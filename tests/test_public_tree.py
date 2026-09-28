from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('public_tree', SOURCE / 'tools/check_public_tree.py')
if spec is None or spec.loader is None:
    raise RuntimeError('Cannot load publication checker.')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PublicTreeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        manifest = json.loads((SOURCE / 'public-files.json').read_text())
        for name in manifest['files']:
            destination = self.root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / name, destination)

    def change_manifest(self, transform):
        path = self.root / 'public-files.json'
        value = json.loads(path.read_text())
        transform(value)
        path.write_text(json.dumps(value))

    def change_status(self, transform):
        path = self.root / 'release-status.json'
        value = json.loads(path.read_text())
        transform(value)
        path.write_text(json.dumps(value))

    def test_current_package(self):
        self.assertEqual(checker.validate(self.root), [])

    def test_application_is_explicitly_blocked(self):
        self.assertTrue(any('release is blocked' in x for x in checker.validate(self.root, True)))

    def test_new_unreviewed_file_fails(self):
        (self.root / 'notes.txt').write_text('Synthetic note')
        self.assertIn('Unreviewed file: notes.txt', checker.validate(self.root))

    def test_missing_file_fails(self):
        (self.root / 'README.md').unlink()
        self.assertIn('Listed file missing: README.md', checker.validate(self.root))

    def test_path_traversal_fails(self):
        self.change_manifest(lambda v: v['files'].append('../outside.txt'))
        self.assertTrue(checker.validate(self.root))

    def test_absolute_path_fails(self):
        self.change_manifest(lambda v: v['files'].append('/outside.txt'))
        self.assertTrue(checker.validate(self.root))

    def test_duplicate_path_fails(self):
        self.change_manifest(lambda v: v['files'].append('README.md'))
        self.assertTrue(checker.validate(self.root))

    def test_case_collision_fails(self):
        self.change_manifest(lambda v: v['files'].append('readme.md'))
        self.assertTrue(checker.validate(self.root))

    def test_symlink_fails(self):
        (self.root / 'link.md').symlink_to(self.root / 'README.md')
        with self.assertRaises(ValueError):
            checker.validate(self.root)

    def test_database_remains_excluded_when_listed(self):
        (self.root / 'synthetic.sqlite').write_text('Synthetic')
        self.change_manifest(lambda v: v['files'].append('synthetic.sqlite'))
        self.assertIn('Excluded file class: synthetic.sqlite', checker.validate(self.root))

    def test_environment_file_remains_excluded(self):
        (self.root / '.env').write_text('SYNTHETIC=true')
        self.change_manifest(lambda v: v['files'].append('.env'))
        self.assertIn('Excluded file class: .env', checker.validate(self.root))

    def test_false_ready_status_fails(self):
        self.change_status(lambda v: v.update(application_readiness='ready'))
        self.assertTrue(checker.validate(self.root))

    def test_missing_gate_fails(self):
        self.change_status(lambda v: v['gates'].pop('authority'))
        self.assertTrue(checker.validate(self.root))

    def test_malformed_json_fails(self):
        (self.root / 'release-status.json').write_text('{')
        self.assertTrue(checker.validate(self.root))

    def test_binary_file_fails(self):
        (self.root / 'README.md').write_bytes(b'\x00\xff')
        self.assertTrue(checker.validate(self.root))

    def test_large_file_requires_review(self):
        (self.root / 'README.md').write_text('x' * 1_000_001)
        self.assertTrue(checker.validate(self.root))

    def test_manifest_must_include_itself(self):
        self.change_manifest(lambda v: v['files'].remove('public-files.json'))
        self.assertTrue(checker.validate(self.root))

    def test_required_document_cannot_be_dropped(self):
        (self.root / 'SECURITY.md').unlink()
        self.change_manifest(lambda v: v['files'].remove('SECURITY.md'))
        self.assertTrue(checker.validate(self.root))


if __name__ == '__main__':
    unittest.main()
