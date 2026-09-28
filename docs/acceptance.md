# Acceptance-driven implementation

The scenarios in ../acceptance/workspace.feature specify expected behavior. They are not implemented step definitions and have not been executed against the application.

For each scenario, create an isolated deterministic fixture, implement the actual user interaction, assert the canonical data and negative effects, and inspect the result at desktop and narrow widths when relevant. Include keyboard interaction and recovery.

Use existing application domain and browser-test infrastructure rather than introduce another test framework solely to parse this feature file. Link scenario IDs to test paths and exact-candidate receipts. Keep NOT RUN explicit until those links exist.

Synthetic-provider tests must never be presented as live-model proof. Live synthetic audio does not establish the physical microphone path. Readiness is scoped to the evidence that actually ran.

The initial release gate requires source/privacy qualification and the core task, conversation, capture, authority, and recovery journeys. Other scenarios can be shipped in measured increments, but missing coverage must remain visible.
