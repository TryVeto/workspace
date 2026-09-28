# Openship deployment integration

Status: approved direction for evaluation. Openship is a deployment adapter candidate, not a replacement for Workspace's release, evidence, or authorization model.

## Decision

Evaluate and adopt Openship for deployable web/service candidates once one Veto-owned application path passes an isolated qualification.

Do not make Openship the runtime for the local Workspace database, the macOS host, browser security boundary, coworker identity, or the source of truth for whether product work is complete.

The useful boundary is:

```text
Veto Work / Mission / Studio candidate
              |
       qualified release manifest
              |
       Deployment adapter
              |
           Openship
              |
 preview / staging / production target
```

Workspace owns why a deployment exists, the exact candidate being reviewed, the acceptance evidence, who authorized promotion, and the returned outcome. Openship owns the mechanics of building, shipping, routing, observing, and rolling back the deployable service.

## Why it fits

Openship's published product and API expose several primitives that match Workspace's direction:

- Git, local-folder, CLI, desktop, API, and agent-triggered deployment paths
- commit-bound deployments and explicit project/environment identities
- immutable/versioned releases and rollback
- preview and production environments
- self-hosted operation and deployment to an operator-controlled server over SSH
- managed domains/TLS and supporting services where needed
- structured CLI/REST interfaces suitable for an adapter rather than UI automation
- Apache-2.0 licensing for Openship-authored code

Those capabilities can remove infrastructure work without changing Veto's higher-level product semantics.

## What Veto must preserve

A successful Openship deployment is not the same thing as a completed Veto task.

For every deployment, Veto should retain:

- originating Work/Mission identifier
- source repository and exact commit or immutable source digest
- build configuration revision
- requested environment and target
- deployment request identity
- provider deployment/release identity
- observed build result
- observed route/health result
- acceptance evidence performed after deployment
- promotion or rollback decision and actor
- unresolved or unknown outcomes

If an API call times out, Veto reconciles the provider state before retrying. It must not infer that a deployment failed or succeeded from the request alone.

## Initial scope

The first integration should be intentionally narrow:

1. One synthetic or non-sensitive service.
2. One explicitly configured Openship project.
3. Preview deployment from an exact commit.
4. Stream or retrieve build status.
5. Resolve the deployed URL.
6. Run Veto-owned acceptance checks against that exact URL.
7. Retain the deployment receipt.
8. Exercise one rollback and verify the resulting release identity.

No production customer environment belongs in the first qualification.

## Adapter contract

The internal interface should remain provider-neutral. A minimal deployment adapter needs operations equivalent to:

- prepare/detect without side effects
- deploy exact source to a named environment
- inspect deployment status and logs
- resolve active release and URL
- list releases
- roll back to an exact prior release
- reconcile an ambiguous request outcome

Provider-specific project IDs and tokens stay in configuration/secret storage. Do not put them in Work descriptions, public repositories, or model prompts unless explicitly required and scoped.

An Openship-specific adapter may use its CLI, SDK, or REST API. Prefer a structured API over browser automation.

## Self-hosted vs cloud

For Veto's current stage, self-hosted or operator-controlled infrastructure is attractive because it preserves portability and makes the deployment path inspectable.

That does not mean self-hosting is automatically safer. Running a deployment control plane, Docker socket access, SSH credentials, TLS, backups, and updates creates an operations responsibility. Qualify the exact mode we intend to use.

If the Openship control plane is self-hosted for GitHub push-to-deploy, use its supported GitHub App path with short-lived installation tokens rather than long-lived personal access tokens where practical.

## Promotion policy

Do not enable automatic production deployment from every push at the start.

A reasonable sequence is:

- branch/PR -> preview
- exact candidate passes Veto acceptance -> eligible for promotion
- explicit authorized promotion -> production
- provider receipt + post-deploy health -> recorded outcome

Later, low-risk services may earn more automation. The authority decision belongs to Veto's release policy, not to whether Openship supports a webhook.

## Exit criteria for adoption

Treat Openship as adopted for a workload only after the qualification proves:

- reproducible deploy from an exact commit
- no secret leakage into logs or artifacts
- deterministic environment/config selection
- correct preview isolation
- health checks against the actual served candidate
- rollback to the intended prior release
- retry/reconciliation behavior after a lost acknowledgement
- acceptable build/deploy latency for that workload
- documented backup and update procedure for the chosen control-plane mode
- no alternate path that bypasses Veto's required promotion policy

Until then, Openship is a promising adapter candidate rather than infrastructure we depend on.
