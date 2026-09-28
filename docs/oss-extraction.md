# Open-source extraction

Status: governing release procedure for publishing the Workspace application from the private operational source tree.

## Decision

Workspace remains one React application. There is no React-free mirror.

React is not the redistribution blocker. The release problem is provenance: the private application contains UI source that was originally assembled in a commercial Untitled UI environment, Veto-specific operating fixtures, machine-local test paths, and private runtime evidence.

The public release must therefore be produced by an explicit, fail-closed extraction rather than by changing the private repository's visibility.

## UI provenance

The Workspace application currently consumes a small set of Untitled UI component roots. Each of those roots has a corresponding implementation in Untitled UI's public MIT-licensed React repository.

The release process uses the public repository as the source of truth for redistributable Untitled UI code. The first reviewed upstream revision is:

- repository: `https://github.com/untitleduico/react`
- revision: `4702dc0ea8d140c3491a85670c7b4fab47b722da`
- license: MIT

The application may keep local changes to those components, but the public version is reconstructed from the pinned MIT upstream and a reviewed Veto-owned patch. Do not publish an ambiguous private component merely because it is byte-similar to an MIT file.

The initial component roots are:

- `components/base/buttons/button.tsx`
- `components/base/input/input.tsx`
- `components/base/textarea/textarea.tsx`
- `components/base/select/select-native.tsx`
- `components/base/dropdown/dropdown.tsx`
- `components/base/checkbox/checkbox.tsx`
- `components/base/avatar/avatar.tsx`
- `components/application/modals/modal.tsx`
- `components/application/file-upload/file-upload-base.tsx`

Every transitive UI dependency used by those files must be admitted from the same reviewed upstream or have its own recorded license and provenance. Preserve the upstream MIT license and attribution.

This procedure does not grant redistribution rights to Untitled UI PRO source that is not independently present in the public MIT repository.

## Instance data boundary

Company state is not application source.

The private application currently has Veto-specific operating seeds and world/bootstrap material mixed into the frontend source tree. Those files must not be copied into the public release.

The public application should start from synthetic fixture data or an empty workspace and load real company state from the user's own authorized storage at runtime.

At minimum, the extraction rejects:

- real relationship, customer, contact, or pipeline fixtures
- company planning backlogs and internal operating plans
- authored company knowledge and private agent instructions
- captures, recordings, screenshots, browser profiles, cookies, and session material
- local databases, recovery exports, and diagnostic bundles
- credentials, tokens, private keys, and provider configuration containing secrets
- machine-specific paths that expose a maintainer's local filesystem
- commercial or otherwise unreviewed third-party source

A public demo fixture must be synthetic in both names and facts. Pseudonymizing a real operating export is not the default release path.

## Source architecture

The long-term application boundary is:

```text
public Workspace code
        |
runtime configuration + authenticated services
        |
workspace/company data supplied by the operator
```

Production Veto instance data belongs below that boundary, not in TypeScript imports compiled into the application bundle.

Where the private app currently imports instance-specific JSON directly, move toward an explicit seed/bootstrap provider. The public provider supplies synthetic data. The Veto operating instance loads its authorized data outside the distributable source package.

Avoid maintaining a public toy application and a separate private product. The same application code should run against different authorized data and configuration.

## Extraction algorithm

For each application release candidate:

1. Freeze an exact private source candidate. Record its revision and any intentionally included local patch set.
2. Create a fresh release directory outside the private repository.
3. Copy only explicitly admitted Workspace-owned source paths.
4. Rehydrate approved third-party UI roots from pinned public upstream revisions.
5. Apply reviewed Veto-owned modifications to those public upstream files.
6. Substitute synthetic public fixtures for private instance data.
7. Scan source and generated output for credentials, local paths, private records, excluded binary classes, and unreviewed files.
8. Generate a provenance manifest containing every redistributed third-party file, upstream revision, license, and local patch identity.
9. Install dependencies from the public release only.
10. Run the public tree check, typecheck, build, and application acceptance suite from that extracted tree.
11. Inspect the built artifact as well as the source tree.
12. Publish only the exact candidate that passed those gates.

Any unknown file, unresolved provenance, scan hit, or candidate drift blocks publication.

## Public/private synchronization

The private application is the active development source until the extraction lane is qualified.

Do not manually copy fixes between two independently evolving codebases. The public repository should receive reviewed release candidates from the extraction process. Public contributions should be applied back through the same application source boundary before the next release.

The goal is one product lineage with different data and distribution boundaries, not two products that happen to share a name.

## Release evidence

A release receipt should include:

- private candidate revision and extraction tool revision
- complete public file manifest
- third-party provenance manifest
- dependency lockfile digest
- private-data scan result
- source and built-artifact scan results
- typecheck/build/test receipts
- clean-install result
- exact public commit/tag
- known unsupported or unqualified capabilities

A release remains blocked until all required gates in `release-status.json` are passed. This document defines the procedure; it does not itself clear any candidate for publication.
