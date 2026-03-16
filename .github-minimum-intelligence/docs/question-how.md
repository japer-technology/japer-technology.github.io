# Question: How?

> [Index](./index.md) · [Questions Overview](./questions.md) · [The Repo Is the Mind](./the-repo-is-the-mind.md)

## How does an idea become an agent?

The central claim of this repository is deceptively simple: intelligence does not have to be hosted *somewhere else*. It can be planted directly inside the place software already lives—the git repository. [The Repo Is the Mind](the-repo-is-the-mind.md) frames that as philosophy, but the codebase reveals something more concrete: an implementation of local sovereignty for AI workflows, built from ordinary developer primitives. The "how" is not magic. It is architecture.

At a high level, Minimum Intelligence fuses four existing systems into one loop:

1. **GitHub Issues** as conversational input.
2. **GitHub Actions** as execution runtime.
3. **A language model provider** as reasoning substrate.
4. **Git commits** as durable memory.

What matters is not each part in isolation; what matters is their composition. The repo turns routine collaboration infrastructure into an operating system for an agent.

---

## How does conversation become computation?

The loop begins when a user opens an issue or posts a comment. The workflow `github-minimum-intelligence-agent.yml` subscribes to both events and launches a job that performs identity checks, setup, and agent execution. Before anything else, it verifies the actor has write-level permissions, which means intelligence is not only embedded—it is governed by repository permissions instead of an external ACL surface. The same mechanism that controls who can push code controls who can instruct the agent.

Then comes a subtle but important transition: the workflow checks out the default branch, installs Bun, runs a lifecycle preinstall script, installs dependencies, and executes the agent entrypoint. In other words, a social event (a comment) is transformed into a deterministic build-and-run pipeline. The prompt is treated like source input.

This is the first major answer to **how**: by expressing AI interaction as CI/CD. A chatbot session is reinterpreted as a reproducible automation run.

---

## How does memory survive tab closures, model swaps, and time?

Conventional assistants tend to forget because their state lives in sessions owned by external platforms. This project replaces session memory with repository state. The README makes this explicit: issue numbers map to session artifacts under `.github-minimum-intelligence/state/`, and those transcripts are committed to git. That means memory inherits every property developers already trust from version control:

- **Durability** (it persists with the repository),
- **Auditability** (you can inspect exactly what was said and changed),
- **Diffability** (you can compare revisions of the agent’s behavior),
- **Recoverability** (history can be restored via normal git operations).

This architecture has a profound consequence: memory is no longer a product feature; memory is a file format under source control. “Long-term context” is not promised by marketing copy—it is guaranteed by commit history.

---

## How does identity emerge instead of being hardcoded?

Minimum Intelligence does something unusual for tooling: it treats identity as a collaborative artifact. The bootstrap content in `.pi/BOOTSTRAP.md` frames first contact not as configuration but as co-creation—name, nature, vibe, style, boundaries. The installer also initializes `AGENTS.md`, and the hatch process writes identity instructions there.

In most AI products, personality is a static preset selected from a dropdown. Here, identity is authored in markdown, versioned, and revisable through normal pull-based workflows. You can literally point to the commit where the agent became itself.

So another answer to **how** is: through *textual constitutionalism*. The agent is shaped by editable rules in the repo, not opaque server-side settings.

---

## How does installation stay minimal while capability stays broad?

The installer script (`MINIMUM-INTELLIGENCE-INSTALLER.ts`) is pragmatic: create missing `.github` directories, copy templates, initialize agent instructions, install dependencies. No control plane, no migration tool, no provisioning dashboard. The workflow for adoption is intentionally close to a developer’s muscle memory: add files, run script, commit, push, open issue.

This low ceremony is essential. The project’s promise is that intelligence should feel like adding a library, not onboarding to a platform. The setup script in the root reinforces this with a one-liner install path.

Minimalism here is not absence of power; it is a design constraint that keeps power legible.

---

## How does governance remain local?

There is a quiet governance model spread across the repository:

- GitHub collaborator permissions gate who can invoke the agent.
- GitHub App tokens scope execution to repository operations.
- Workflows, prompts, and lifecycle code remain inspectable and modifiable.
- Every meaningful effect is written back into the repo.

That creates a locality principle: policy, behavior, and history are co-located with the codebase they affect. This matters for regulated teams, for open-source maintainers, and for any developer who wants AI assistance without surrendering operational control.

---

## How does this change the developer’s relationship with AI?

The deeper shift is psychological and procedural.

In the typical model, developers context-switch into an AI product, export answers, and manually reconcile them with code. In this model, the agent enters the developer’s existing habitat. Issues become prompts. Pull-style history becomes memory. Workflows become runtime.

The result is not merely convenience. It is a redefinition of interface boundaries:

- The **repo is the UI**.
- The **commit graph is the memory substrate**.
- The **workflow runner is the execution engine**.
- The **agent prompt files are the governance layer**.

By collapsing those boundaries, Minimum Intelligence turns AI from an external consultant into an internal collaborator whose actions are naturally bounded by the same systems humans already use.

---

## How far can this pattern go?

If we treat this repository as a reference architecture rather than a one-off tool, its broader implications are significant:

- Any team can encode domain-specific agent behavior as versioned policy.
- Any conversation can become inspectable institutional memory.
- Any improvement to the agent can ride normal code-review pathways.
- Any rollback of bad behavior can be performed with normal git operations.

This is a path toward **repository-native intelligence** as a general software pattern: AI agents instantiated per repo, governed per repo, and remembered per repo.

---

## Final answer

So, how does it work?

It works by refusing new infrastructure and reinterpreting old infrastructure:

- issues as chat,
- actions as runtime,
- markdown as identity,
- git as memory,
- commits as continuity.

Minimum Intelligence is compelling not because it invents a new platform, but because it reveals that the platform developers needed was already there. The repository was never just a place to store code. With the right loop, it becomes a place where intelligence can be born, shaped, audited, and trusted.
