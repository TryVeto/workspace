from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path, PurePosixPath

REQUIRED = {
    'README.md', 'LICENSE', 'NOTICE', 'CONTRIBUTING.md', 'SECURITY.md',
    'AGENTS.md', 'release-status.json', 'docs/release-readiness.md',
    'docs/architecture.md', 'docs/experience-contracts.md', 'docs/oss-extraction.md',
    'acceptance/workspace.feature', 'tools/check_public_tree.py',
}
GATES = {
    'source_identity', 'third_party_rights', 'private_data_separation',
    'clean_install', 'core_workflow', 'authority', 'voice', 'native_packaging',
}
DISALLOWED_SUFFIXES = {
    '.db', '.sqlite', '.sqlite3', '.mp4', '.mov', '.webm', '.wav', '.mp3',
    '.pem', '.key', '.p12', '.pfx', '.woff', '.woff2', '.ttf', '.otf',
}
IGNORED_DIRECTORIES = {'.git', '__pycache__', '.pytest_cache'}


def checked_path(value: object) -> str:
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('Manifest paths must be nonempty POSIX-relative strings.')
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ('.', '..', '') for p in value.split('/')):
        raise ValueError('Manifest paths must not escape or contain empty components.')
    if ':' in path.parts[0]:
        raise ValueError('Drive-qualified paths are not allowed.')
    return value


def enumerate_files(root: Path) -> set[str]:
    result: set[str] = set()
    pending = [root]
    while pending:
        parent = pending.pop()
        for item in parent.iterdir():
            relative = item.relative_to(root).as_posix()
            if item.is_symlink():
                raise ValueError(f'Symlinks are not allowed in this package: {relative}')
            if item.is_dir():
                if item.name not in IGNORED_DIRECTORIES:
                    pending.append(item)
                continue
            if not item.is_file():
                raise ValueError(f'Non-regular file: {relative}')
            result.add(relative)
    return result


def validate(root: Path, require_application: bool = False) -> list[str]:
    root = root.resolve(strict=True)
    errors: list[str] = []
    actual = enumerate_files(root)
    try:
        manifest = json.loads((root / 'public-files.json').read_text(encoding='utf-8'))
        if not isinstance(manifest, dict) or set(manifest) != {'schema_version', 'files'}:
            raise ValueError('Invalid public-files.json shape.')
        if type(manifest['schema_version']) is not int or manifest['schema_version'] != 1:
            raise ValueError('Unknown file-manifest version.')
        if not isinstance(manifest['files'], list):
            raise ValueError('File manifest must contain a list.')
        paths = [checked_path(p) for p in manifest['files']]
        if len(paths) != len({p.casefold() for p in paths}):
            raise ValueError('Duplicate or case-colliding paths in manifest.')
        admitted = set(paths)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'Manifest: {exc}']
    if 'public-files.json' not in admitted:
        errors.append('The file manifest must list itself.')
    errors.extend(f'Required file absent from manifest: {p}' for p in sorted(REQUIRED - admitted))
    errors.extend(f'Unreviewed file: {p}' for p in sorted(actual - admitted))
    errors.extend(f'Listed file missing: {p}' for p in sorted(admitted - actual))
    for name in sorted(actual & admitted):
        path = root / name
        if path.suffix.lower() in DISALLOWED_SUFFIXES or path.name.startswith('.env'):
            errors.append(f'Excluded file class: {name}')
            continue
        if path.stat().st_size > 1_000_000:
            errors.append(f'File requires separate size review: {name}')
            continue
        try:
            text = path.read_text(encoding='utf-8')
            if '\x00' in text:
                errors.append(f'Binary content in text package: {name}')
        except UnicodeError:
            errors.append(f'Non-UTF-8 file: {name}')
    try:
        state = json.loads((root / 'release-status.json').read_text(encoding='utf-8'))
        expected = {'schema_version', 'package_kind', 'application_source_included', 'application_readiness', 'gates'}
        if not isinstance(state, dict) or set(state) != expected:
            raise ValueError('Invalid release-status.json shape.')
        if type(state['schema_version']) is not int or state['schema_version'] != 1:
            raise ValueError('Unknown release-status version.')
        if state['package_kind'] not in ('publication-preparation', 'application'):
            raise ValueError('Unknown package kind.')
        if type(state['application_source_included']) is not bool:
            raise ValueError('Source inclusion must be a boolean.')
        if state['application_readiness'] not in ('blocked', 'ready'):
            raise ValueError('Unknown application-readiness value.')
        gates = state['gates']
        if not isinstance(gates, dict) or set(gates) != GATES:
            raise ValueError('The complete named gate set is required.')
        if any(v not in ('not_run', 'blocked', 'passed') for v in gates.values()):
            raise ValueError('Unknown gate status.')
        ready = (state['package_kind'] == 'application'
                 and state['application_source_included']
                 and all(v == 'passed' for v in gates.values()))
        if state['application_readiness'] == 'ready' and not ready:
            errors.append('Application readiness contradicts the recorded gates.')
        if require_application and (state['application_readiness'] != 'ready' or not ready):
            errors.append('Application release is blocked; preparation checks are not application qualification.')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Release status: {exc}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description='Check the publication package, not application behavior or legal clearance.')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--require-application', action='store_true')
    args = parser.parse_args()
    try:
        errors = validate(args.root, args.require_application)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('Preparation package checks passed. No application or security qualification is implied.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
