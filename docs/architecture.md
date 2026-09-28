# Architecture

Status: product and integration contract. This document is not evidence that the public checkout implements the application.

## Preserve the existing application

The application under preparation already has a React/TypeScript interface, a Python/SQLite local service, a thin macOS host, and Codex integration. Source publication should extract and qualify that application. Do not rebuild it as a new demo merely to obtain a public repository.

## Ownership

| Data | Owner |
| --- | --- |
| Tasks, outcomes, assignments, dates, completion | Work |
| Channels, DMs, discussions, messages | Comms |
| Authored documents and exact revisions | Knowledge/document service |
| Engagement, contacts, commitments | Relationships |
| Maintained claims, questions, forecasts | World |
| Original captures and source artifacts | Capture/source library |
| Authority, grants, approvals, action receipts | Authorization/action service |
| Temporary reasoning and execution | Runtime adapter |

Home, global commands, shelves, browser panes, and voice are entry points over these owners. They must not create competing copies. A third-party memory provider may index records; removing that provider must not delete authoritative records.

## Composition

A shared application shell provides navigation, command entry, a context-aware creation composer, and a right-hand inspector. Route state controls navigation; draft state survives closing overlays and returning to a surface. A task shelf and full task page refer to the same record.

The global plus opens the creation composer without navigation. The plus inside a composer adds context or attachments. These are different commands with distinct accessible labels.

## Runtime and identity

Coworker identity is versioned separately from the provider model, runtime session, and voice. A runtime request binds an authenticated user, coworker definition, conversation, context permissions, capability policy, and exact source versions.

Voice is an input/output modality on a canonical conversation. It must not create a separate generic assistant while the UI displays a coworker's name. Unbound voice must either ask for a recipient or explicitly identify itself as a distinct assistant with its own restricted policy.

Reuse qualified Codex interfaces for execution; do not assume every hosted feature or API exists in every native runtime version. Preserve the runtime version and configuration in qualification receipts. Switching providers or billing paths requires an explicit configuration decision.

## Evidence and action

A capture preserves an observation. A task defines requested work. A document revision is an artifact. A forecast is an expectation, not a fact. A decision records authorized adoption. Links connect these meanings without collapsing them.

Actions pass through authenticated authorization, exact input binding, execution, and outcome reconciliation. Read and write access are separate from permission to disclose information. Browser, voice, and shell paths cannot be back doors around the same policy.

## Persistence and recovery

Persist commands and drafts before dispatching work. Use version checks and idempotency identities to prevent duplicate or stale changes. An interrupted provider operation with an unknown outcome remains unresolved until reconciled. Closing an audio channel or dismissing a card cannot establish business completion.

## Publication boundary

Application source and synthetic examples can be public after their rights and security reviews. Real captures, customer data, correspondence, credentials, private instructions, diagnostic exports, and commercial component source are excluded unless separately and explicitly cleared. Build artifacts need the same scrutiny as source.
