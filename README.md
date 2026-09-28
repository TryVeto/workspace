# Workspace

**A shared workspace for people and AI coworkers.**

Bring work, conversations, documents, relationships, and evidence into one place. Start with an instruction, carry the work forward with a coworker, and return to the actual result—not a trail of disconnected chats.

> **Release status: public preparation, not the application release.** This repository currently contains the open-source release contract, architecture, contribution guidance, and acceptance specifications. The current application is being separated from restricted third-party source and private operating data. It is not yet available to install from this repository. Documentation is not proof of implemented behavior.

The previous project at this address is preserved as [Workspace Classic](https://github.com/TryVeto/workspace-classic). That is a different, older runnable harness. Its history has not been deleted. Existing Classic clones must update their remote; reusing this repository name replaces the old redirect.

## The product

Workspace is built around six connected places, not six independent databases:

| Place | Purpose |
| --- | --- |
| **Home** | Start work, resume it, and see what needs your attention. |
| **Work** | Own outcomes, tasks, objectives, experiments, and their actual completion. |
| **Comms** | Talk with people and coworkers in persistent, scoped conversations. |
| **Knowledge** | Write and maintain documents, instructions, and decisions. |
| **Relationships** | Understand people, organizations, commitments, and follow-ups. |
| **World** | Maintain evidence-linked understanding, questions, and outlooks. |

Global capabilities connect these places: command and capture, contextual task shelves, voice, and reusable work definitions. Browser integration, forecasting, simulation, and longer-running agent work must earn their release status through complete, tested workflows; they are not claimed as shipped here.

## What makes it different

**One object, multiple ways in.** A task opened from Home and Work is the same task. A conversation beside a document is the same conversation available in Comms.

**Coworkers have continuity.** Identity and admitted instructions are versioned independently of the model, voice, or runtime thread used to perform a turn.

**Tools carry work forward; the application governs consequences.** Context, source access, delegated capabilities, exact approvals, and receipts are application responsibilities—not promises hidden in a prompt.

**Evidence is inspectable.** A capture, a claim, a forecast, and an approved decision are different objects. They can be linked without turning one into another.

**Useful autonomy, not continuous noise.** Posting a message does not wake every coworker. Work should return a result, a specific question, or an actionable exception.

## Architecture

The current implementation under preparation uses a React/TypeScript interface, a local Python/SQLite service, a thin macOS host, and the official Codex App Server. Publication will preserve the existing application rather than replace it with a new demonstration.

The intended ownership boundary is straightforward:

```text
Interface and native host
          |
Authenticated application services
          |
Records + source access + action policy + receipts
          |
Scoped runtime and provider adapters
```

The app owns durable business meaning. Runtime adapters supply cognition and execution. A search or memory provider is replaceable and must not become the only home of a task, document, conversation, or approved decision.

Read the [architecture](docs/architecture.md), [experience contracts](docs/experience-contracts.md), and [release gates](docs/release-readiness.md).

## What can I run today?

There is **no application quickstart in this checkout yet**. Do not use a production company database or copy a private working tree into this repository to make it run.

Once the supporting files are present, the preparation checks require Python 3.11 or later and no external services:

```sh
python3 -m unittest discover -s tests -v
python3 tools/check_public_tree.py
```

These checks qualify the publication package only. They do not establish application functionality, browser security, voice quality, or successful agent execution. Product acceptance scenarios are separately listed under `acceptance/` and remain **NOT RUN** until linked to implementation test receipts.

## Road to the first application release

1. Freeze an exact source candidate and inventory its dependencies, assets, and rights.
2. Keep verifiably open-source components; replace or obtain redistribution rights for restricted components. Preserve required notices.
3. Move instance data, conversations, captures, credentials, private reference material, and diagnostics outside the release tree. Use synthetic demo data.
4. Prove a clean install and an end-to-end task/conversation/capture journey in an isolated environment.
5. Qualify access controls, approvals, voice identity, recovery, and packaging before claiming those capabilities.

The full application source release is **blocked pending those gates**. A green documentation check does not remove that block.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Small, tested changes with an explicit owner and a clear user outcome are preferred. Coordinate architectural changes before introducing a second runtime, memory system, or copy of an existing object.

Use synthetic fixtures. Do not attach real email, customer information, credentials, browser profiles, or personal recordings to public issues or pull requests.

## Security

Read [SECURITY.md](SECURITY.md). Do not report exploitable details or secrets in public issues. The repository's public status does not make an experimental build suitable for sensitive work.

## License

Original material published here is licensed under [Apache-2.0](LICENSE), except where an explicit notice says otherwise. Third-party components retain their own terms. This license does not relicense restricted source kept outside this repository or grant rights to the Veto name, marks, or private operating data.
