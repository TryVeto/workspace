# Contributing

Workspace is in public release preparation. The application itself is not yet in this repository. Contributions should help produce a usable, auditable release rather than grow a separate prototype.

## Before changing anything

Read README.md, docs/architecture.md, docs/release-readiness.md, and the relevant acceptance scenario. Establish whether your change is a product decision, source extraction, an implementation, or qualification. Do not report one as another.

For larger changes, describe the user outcome and the existing owner you will extend. Reuse the current runtime and record contracts. A second task database or a parallel voice identity system requires an explicit architectural decision.

## Local checks

Python 3.11 or later is sufficient for this preparation package:

```sh
python3 -m unittest discover -s tests -v
python3 tools/check_public_tree.py
```

The checks are offline and do not use models, provider accounts, or live company records. Product scenarios are not executable acceptance tests yet.

## Pull requests

Explain what changed, why it matters, which checks actually ran, and what remains untested. Include failure/recovery behavior and accessibility when relevant. Link the changed user contract. Keep changes focused; do not bundle unrelated generated files.

All new files require an explicit entry in public-files.json. That list is a review aid, not evidence that a file is safe or licensed. Review actual bytes, provenance, and rights before adding an entry. Do not automate approval of every file discovered in a private checkout.

Use synthetic fixtures and your own authorized development accounts. Do not run an unreviewed contribution with real credentials. CI must not give secrets to untrusted pull requests.

## Rights and attribution

Submit only work you are authorized to contribute under the repository license. Preserve upstream notices. Identify copied or adapted material and its precise upstream source and license. A nearby MIT notice does not establish that an entire commercial UI kit is MIT-licensed.

Do not upload private company documents, personal captures, recordings, email, credentials, session cookies, browser profiles, recovery exports, or restricted component source. Keep operational data outside the application repository.

## Review standard

Maintain existing outcomes and ownership boundaries. Do not mark a task complete because a model said it is done, or mark an action successful because it was approved. Require observable outcomes and retain uncertainty when necessary.

Be clear, generous, and specific in review. See CODE_OF_CONDUCT.md. Maintainers may decline adjacent integrations or support obligations that do not advance the maintained product.
