# Experience contracts

These are implementation decisions proposed for the reviewed experience. They are not a claim that the current public checkout implements them.

## Capture explorer

Expose one maintained capture library through the global command surface and a visible Captures entry. Keep the existing capture identities and source-storage owner. A World/Command entry may link to it; it must not create another copy of the library.

The default view lists recent permitted captures with title, source application/page, capture time, type, processing status, and linked work. Offer grid and list views, full-text search, and filters for time, type, source, and linked/unlinked work. Distinguish indexed records from unavailable or still-processing media.

Opening a capture uses the contextual shelf. Show its note, original and annotated evidence, video timeline when present, selected frames with timestamps, and linked tasks. Expand for deeper inspection. Creating work references exact capture and evidence identities; it does not turn the raw capture into a task or duplicate its files.

Treat user notes, source text, and model interpretations separately. Keep original evidence immutable under ordinary editing; annotations and redactions are derived versions. Archiving an item changes discoverability, not the task's completion. Export and sharing require an explicit audience.

## Global creation composer

Global plus opens a compact, centered composer above a blurred or dimmed page. Retain the current route, scroll position, selected object, and unsent writing. Reduced-transparency and reduced-motion settings receive a simple alternative.

Use the shared draft and submission contract. Task and Chat are explicit modes. The inner plus adds attachments/context. Escape dismisses the innermost open control first, then the overlay. Restore focus to the trigger. Drafts survive dismissal; closing is not submission.

Submitting a task creates one canonical Work record and opens its shelf after a confirmed save. Submitting a chat opens the selected canonical DM and sends exactly once. Failed saves retain the draft. Do not automatically create a blank output artifact and show it as progress.

## Assignment

A fresh global task draft starts unassigned. Preserve a selection within its draft. Do not silently reuse a prior task's assignee for every future draft. Explicit contextual entry from a coworker profile or DM may prefill that coworker visibly.

Selecting an owner does not send a message or grant access. An unassigned task may be saved without dispatching a random coworker. Chat and voice need an explicit or clearly displayed contextual recipient. People in an external address book are not automatically workspace members or runnable agents.

## Natural-language dates

Recognize clear due-date expressions in the composer and display an editable date chip. Preserve original text, reference timestamp, timezone, date precision, and whether the date was inferred or explicitly chosen.

Date-only values remain date-only. Do not invent midnight UTC. A due date is not a scheduled start, reminder, calendar invitation, or external commitment. Explicitly chosen dates take precedence over later background inference.

Use deterministic parsing for familiar date phrases; do not invoke a model on every keystroke. Complex interpretation may produce a proposal through the existing coworker/runtime path. Mentioning tomorrow's document does not necessarily make tomorrow the deadline.

## Permissions

Display effective capabilities and their source. Offer understandable presets backed by concrete server policy, not a cosmetic 'allow everything' control. A broad preset can only operate inside the current user's authority and the workspace's non-overridable limits.

Separate read scope, reversible in-scope changes, and actions requiring exact approval. Show account, destination, payload, relevant source revision, expiry, and requested consequence when approval is necessary. The same operation has the same policy whether requested by typing, voice, browser, or a scheduled mission.

## Voice

Dictation writes into the current draft and does not send. Conversation speaks with the selected coworker in the existing conversation. Resolve identity, role, admitted instruction version, capabilities, and provider voice on the server before showing a named connected call.

A missing or incompatible identity must produce an explicit error or clearly labeled fallback; it must never appear as a named coworker with generic identity. Stable per-coworker audible identity is separate from user device and accessibility preferences.

Use actual transport/speech states for Connecting, Listening, Thinking, and Speaking. Support captions, mute, interruption, device errors, minimize, and End. Minimizing preserves the call; End closes media and native realtime activity without fabricating completion of unresolved actions.

Return transcript and action receipts to the original conversation. A voice utterance cannot change policy or authorize a different payload merely by sounding like 'yes'. Exact consequential confirmations remain inspectable and bound to the operation.
