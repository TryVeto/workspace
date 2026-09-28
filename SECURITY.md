# Security

## Current support status

This repository is a publication-preparation package. No application release or production-security guarantee is offered by its passing tests. Do not connect experimental candidates to a real password manager, inbox, customer data, or unrestricted shell until the relevant execution paths are qualified.

## Report privately

Use GitHub **Security → Report a vulnerability** for this repository. If the private-reporting control is unavailable, open a public issue containing only a request for a private contact route. Do not include exploit details, secrets, customer data, recordings, or authentication material in that public request.

Include the affected revision, an isolated synthetic reproduction, expected boundary, observed outcome, and likely impact. Use the minimum evidence necessary. This project does not promise a response-time service level or bug bounty.

## Required security boundaries

Application services must derive the caller from an authenticated connection. A model-supplied actor ID is not authentication. User authority, record access, task delegation, runtime restrictions, and provider permissions must all allow the operation.

Consequential actions require an enforceable authorization path: exact operation and arguments, destination/account, relevant revisions, applicable grant or approval, expiry, one-use claim where required, and a provider outcome receipt. An approval is not a success receipt. A timeout is not permission to retry blindly.

Text, voice, browser, shell, plugins, and memory are not exceptions to those rules. A read capability can still disclose private information, so read scope and output audience matter. Unknown tools and callbacks must not inherit permission.

Captures and derived material must retain access scope. Filesystem and archive paths must be validated, not trusted because they originated from a manifest. Keep private material outside the public release and web-static roots.

A loopback-only, single-user service is not a hosted multi-user authorization design. Hosted access requires explicit identity, per-resource permissions, tenant isolation, protected credentials, and a separate security qualification.

## Disclosure and releases

Resolve confirmed vulnerabilities in a reviewed candidate and record the affected revisions. Publish sanitized advisories without disclosing customer material. Maintain signed distributable provenance and an update process before recommending native binaries for sensitive use.
