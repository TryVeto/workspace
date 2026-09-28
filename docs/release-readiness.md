# Application release readiness

**Current disposition: BLOCKED.** The public repository is preparation material, not the extracted application.

## Gates

| Gate | Evidence required | Current status |
| --- | --- | --- |
| Source identity | Exact source revision and reviewed extraction manifest; no unrelated parent history | NOT RUN |
| Third-party rights | Per-file/package provenance and redistribution permission, required notices | BLOCKED |
| Private data separation | Reviewed source, fixtures, assets, diagnostics, and history; synthetic public examples | NOT RUN |
| Clean install | Reproducible install from this repository on a supported clean machine | NOT RUN |
| Core workflow | Task, canonical conversation, result, capture, and recovery behavior | NOT RUN |
| Authority | Authenticated caller and scope, deny cases, exact approvals, no alternate execution bypass | NOT RUN |
| Voice | Actual selected identity, text/voice continuity, caption/media lifecycle, action receipts | NOT RUN |
| Native packaging | Signed build provenance, update path, microphone/download/session behavior | NOT RUN |

## Third-party source

The implementation's private source documentation identifies commercial UI components. The presence of an MIT notice in the tree does not establish that all copied components are MIT-licensed. Match every redistributed component to its provenance and exact license. Keep verified open-source files; replace the rest independently or obtain explicit redistribution permission.

Untitled UI distinguishes its open-source components from commercial source in its [license agreement](https://www.untitledui.com/license). Do not infer permission from a purchase or from the ability to download a component.

Packages, fonts, icons, images, examples, and reference material require their own checks. Dependencies named in a design proposal are not evidence that the exact installed package has compatible terms.

## Extraction procedure

Work from an identified candidate into a separate release directory. Use explicit allowed paths and inspect bytes before committing. Do not flip an existing operational repository to public. Do not copy captured screens, contact data, email, database snapshots, private instructions, or source archives into demo fixtures.

Preserve applicable attribution and provenance without importing private Git history. Remove machine-specific setup assumptions. Create synthetic data and a fresh-install guide. Review the distributable build as well as the source.

## Qualification receipts

Every claimed test result should name the candidate revision, configuration, fixture, command, result, and scope. Keep mock-provider tests, live synthetic tests, and physical-device tests distinct. A recorded screenshot is not proof of permissions enforcement.

Preparation-package tests verify documentation, file admission rules, and declared release state only. They are not application acceptance. The Gherkin scenarios intentionally have no passing status until bound to executed tests.

## Repository move

The former public harness is now [Workspace Classic](https://github.com/TryVeto/workspace-classic). Existing Classic clones should use:

```sh
git remote set-url origin https://github.com/TryVeto/workspace-classic.git
```

Run that only in a clone of the Classic project. Do not retarget the active private application or a parent operations repository. GitHub documents that [reusing the old name disables the rename redirect](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository).

## What changes readiness

Only completed gates with reviewable evidence can change application readiness. Editing release-status.json is bookkeeping, not authorization. A maintainer must approve the actual application candidate and its publication scope before upload.
