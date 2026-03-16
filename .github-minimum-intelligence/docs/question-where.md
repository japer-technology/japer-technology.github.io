# Question: Where?

> [Index](./index.md) · [Questions Overview](./questions.md) · [The Repo Is the Mind](./the-repo-is-the-mind.md)

## Where does intelligence actually live?

If *[The Repo Is the Mind](the-repo-is-the-mind.md)* is the thesis, then this repository is its field evidence. The “where” is not metaphorical. Minimum Intelligence answers it with a physical address: inside the repository’s own boundaries, executed by the same automation that already builds and ships code.

Most AI tooling treats your codebase like an export format. You copy snippets out, paste context in, and hope nothing important gets lost in transit. This project refuses that architecture. Here, the repo is not an attachment to intelligence—it is the substrate of intelligence.

---

## Where does runtime happen? In your CI, not in someone else’s product

The workflow template (`.github-minimum-intelligence/install/github-minimum-intelligence-agent.yml`) is explicit: issue events and issue comments trigger a job, collaborator permissions are checked, the repository is checked out, Bun is installed, and the agent scripts run locally in the Actions runner.

That matters because it collapses the distance between “assistant” and “environment.” The agent doesn’t infer your project structure from a pasted tree; it executes in a fresh clone of the actual tree. It sees what your developers would see at HEAD.

In practical terms, the “where” of execution is:

- **GitHub Actions runner filesystem** (real files, real commands)
- **Your repository checkout** (not a mirrored index)
- **Your repo-scoped token permissions** (not a vendor-specific ACL)

This is infrastructure locality: computation happens where governance already exists.

---

## Where does memory persist? In versioned state under git

The strongest architectural move in this repo is that memory has a directory.

The orchestrator (`.github-minimum-intelligence/lifecycle/agent.ts`) persists issue-to-session mappings and session transcripts under `.github-minimum-intelligence/state/`. The README repeats the same mapping model: issue number → state file → session transcript. This is not decorative documentation; it is the mechanism of continuity.

So “where memory lives” is no longer a hand-wavy concept about context windows. It lives in:

- `.github-minimum-intelligence/state/issues/<number>.json`
- `.github-minimum-intelligence/state/sessions/<session>.jsonl`

Because these artifacts are committed, memory inherits git properties by default: inspectability, rollback, branchability, and diffability. If context drifts, you can audit it like any other code-adjacent artifact. “Long-term memory” becomes a repository primitive, not a hosted feature.

---

## Where does identity live? In checked-in text you can review

The project makes a second locality claim: personality is also repository-native.

`BOOTSTRAP.md` and `APPEND_SYSTEM.md` define how the agent is “hatched” and how behavior evolves. `AGENTS.md` stores identity as Markdown: name, nature, vibe, purpose, and operating guidance. The installer even initializes this file path as part of setup.

That means the agent’s operating self is located in files, not hidden behind provider-side prompts you cannot inspect. Identity is editable by pull request, attributable by commit author, and reversible by reset. In other words, the agent’s “who” lives where the team already negotiates everything else: in text under source control.

---

## Where does authorization live? In existing GitHub collaboration semantics

The workflow’s `Authorize` step checks the actor’s collaborator permission and rejects unauthorized invocations with a negative reaction. The system does not invent a parallel user model. It simply reuses repository permissions (admin/maintain/write).

That design choice answers “where is trust enforced?” with impressive restraint: in GitHub’s existing permission model. You do not manage a second, drifting identity system for AI access. The assistant is bounded by the same institutional guardrails as human contributors.

---

## Where does installation land? As a folder, not an onboarding process

The installer script (`MINIMUM-INTELLIGENCE-INSTALLER.ts`) shows the project’s ergonomics: copy workflow template, copy hatch template, initialize `AGENTS.md`, install dependencies. The `setup.sh` script inside `.github-minimum-intelligence/script/` mirrors that one-command posture.

This is subtle but essential. By making installation file-centric, the project ensures the answer to “where is the product?” remains simple: in `.github-minimum-intelligence/` plus generated `.github/` workflow/template files. The “platform” is a commit.

---

## Where is the boundary between model and system?

[the-repo-is-the-mind.md](the-repo-is-the-mind.md) describes a clean split:

- LLM handles planning and synthesis.
- `pi` tool surface handles concrete actions.

That separation clarifies location in two senses:

1. **Reasoning location**: model endpoint (provider of choice).
2. **Effect location**: your repository runtime and git history.

The model may be remote, but consequences are local and versioned. This decoupling preserves sovereignty: you can swap providers while keeping memory format, workflow loop, and governance surface stable.

---

## Where does collaboration happen over time?

This repository reframes issues as durable conversations and commits as procedural memory. A comment is not a transient chat bubble; it is an event that triggers reproducible automation, emits artifacts, and extends a traceable narrative.

That means collaboration has one canonical location instead of three scattered ones:

- discussion in Issues,
- execution in Actions,
- continuity in Git.

The agent is “in” the same places the team already uses. No secondary workspace is required.

---

## Final answer

Where is the mind?

In this architecture, it is distributed but coherent:

- **in workflows** for action,
- **in state files** for memory,
- **in markdown** for identity,
- **in permissions** for governance,
- **in commits** for truth over time.

Minimum Intelligence’s deepest claim is that intelligence should not orbit the repository as an external service. It should inhabit the repository as a first-class, auditable participant. This codebase demonstrates that claim concretely: the “where” of AI is not a dashboard, not a chat tab, not a vendor silo.

It is the repo itself.
