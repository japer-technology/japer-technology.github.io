# The Repo Is the Mind

> [Index](./index.md) · [Questions Overview](./questions.md) · [README](../../README.md)

> A repository is more than files - it's code, conversation, constraints, and history

Many AI tools can hover around Git: they can read files, suggest changes, even generate patches. But they remain outsiders. They don’t live with the code, they don’t carry the project’s conversation history inside the repo, and they don’t accumulate the intent, constraints, tradeoffs, and decisions that shaped the work over time. That gap is the real problem. The breakthrough isn’t merely AI that can see code - it’s AI that remembers the why behind the code: the false starts, the hard choices, and the reasoning that got you here. Without that memory, it isn’t collaboration; it’s starting from zero every time.

The `pi` coding agent and the Minimum Intelligence framework eliminate that context gap by embedding the AI directly in the repository - not as a service integration, but as a versioned dependency that operates inside your existing Git, Actions, and Issues infrastructure.

#### What Where How Who When Why

## What - A `devDependency`, Not a Platform

> An npm package you install in your tree - no hosted backend, no OAuth handshake, no new trust boundary beyond what you configure in Actions YAML.

`@mariozechner/pi-coding-agent` is an npm package. Minimum Intelligence is a repo-local configuration layer. There is no hosted backend, no OAuth handshake, no tenant isolation to think about.

You install it. It runs in your tree. That's the entire vendor relationship.

This means standard supply-chain practices apply directly: version pinning, lockfile auditing, vendoring, forking. The agent's capabilities are scoped to what your workflow file grants it - the same GITHUB_TOKEN permissions model you already manage. No new trust boundary is introduced beyond what you explicitly configure in your Actions YAML.

If the upstream package disappears tomorrow, your pinned version still works. If you disagree with a behavioral change, you fork. The dependency model gives you the same leverage here as it does with any other package in your stack.

---

## Where - Colocation With the Worktree

> Inside a GitHub Actions runner with a full checkout of your repository - direct filesystem access, no API abstraction layer, no context-window packing heuristics.

The agent runs inside a GitHub Actions runner with a full checkout of your repository. It has direct filesystem access to your worktree - no API abstraction layer, no context-window packing heuristics on your end.

Concretely:
- **Runtime**: GitHub Actions (or any CI environment you wire up)
- **Persistent memory**: Git history - commits, branches, tags
- **Conversation state**: GitHub Issues and issue comments
- **Configuration**: Repo-local Markdown and YAML files checked into the tree

The implications for context fidelity are significant. The agent doesn't need you to explain your monorepo layout or paste your `tsconfig.json`. It reads `tsconfig.json`. It runs `find`. It greps your source. The full project graph is available without serialization overhead or token-budget tradeoffs.

This also means the agent's actions produce first-class Git artifacts. Every change is a commit. Every commit has a hash, an author, a diff. Your existing branch protection rules, CODEOWNERS, and review workflows apply unchanged.

---

## How - LLM Reasoning + `pi` Tool Execution

> The LLM reasons and plans; `pi` executes - a ReAct-style agent loop where the tool surface is your actual development environment, not a sandboxed approximation.

The architecture cleanly separates cognition from action.

The LLM handles planning, reasoning, and code generation - the probabilistic reconstruction of plausible solutions from its trained weights. On its own, it produces text. It cannot execute.

`pi` provides the execution layer: a tool harness that exposes filesystem operations, shell access, search, and Git commands to the LLM as callable functions. The interaction loop is:

1. LLM receives the issue body and repo context
2. LLM emits a tool call (e.g., `read`, `bash`, `edit`, `write`)
3. `pi` executes the call and returns the result
4. LLM reasons over the result and emits the next action
5. Loop until the task resolves - typically with a commit and/or comment

This is a standard ReAct-style agent loop, but the critical differentiator is that the tool surface is your actual development environment, not a sandboxed approximation. The agent runs real commands, in your real repo, with real consequences tracked by real version control.

---

## Who - Agent Identity as Checked-In Config

> A Markdown persona file committed to your repository - diffable, reviewable, and governed by your normal pull request process.

On initialization, you "hatch" the agent by opening an issue and defining its persona through dialogue. The result is a Markdown file committed to the repository - typically in `.github-minimum-intelligence/` - that governs the agent's tone, priorities, and behavioral constraints.

This is configuration-as-code for agent personality. It's diffable, reviewable, and subject to your normal PR process. You can:
- `git log` the persona file to trace behavioral evolution
- `git blame` to see who changed what and when
- branch it to A/B test different agent personalities
- revert it if a change produces worse interactions

There is no hidden system prompt controlled by a vendor. The full instruction set is in your tree, readable and modifiable by anyone with repo access.

---

## When - Stateless Execution, Stateful History

> Each invocation is a fresh process; continuity is a property of the repository, reconstructed from durable artifacts - issues, commits, and repo state at HEAD.

Each agent invocation is a fresh process - no warm session, no in-memory conversation cache. State is reconstructed from durable artifacts: the issue thread, the commit log, the repo contents at HEAD.

This maps cleanly to async workflows. There is no session timeout, no "conversation expired" error, no context window that silently truncated your earlier messages. You can:

- Open an issue, get a response, disappear for a month
- Reply with new requirements; the agent reads the full thread and current repo state
- Reference commits made in the interim; the agent sees them in `git log`

Continuity is a property of the repository, not of the agent process. As long as Git history and the issue thread exist, the agent can resume with full fidelity.

---

## Why - Sovereignty and Auditability by Default

> Repository-native AI keeps the codebase as the primary system - auditable, sovereign, and under the same governance as everything else you ship.

The practical case is straightforward:

| Concern | How it's addressed |
|---|---|
| **Data sovereignty** | Code never leaves your repo/runner infrastructure |
| **Auditability** | Every agent action is a Git commit with full diff |
| **Vendor lock-in** | npm dependency - pin, fork, or replace at will |
| **Access control** | Standard GitHub permissions, branch protection, CODEOWNERS |
| **Reproducibility** | Agent behavior is deterministic given the same model + config + repo state |
| **Offline/air-gapped** | Runs anywhere you can host a runner and reach an LLM endpoint |

But the architectural argument runs deeper than any checklist. Centralizing AI behind a platform means your codebase becomes a second-class citizen in someone else's system. Repository-native AI inverts that: the codebase is the primary system, and the AI is a tool within it - subject to the same governance, the same review process, and the same version control as everything else you ship.

The repository is already where your team coordinates, where decisions are recorded, and where the canonical state of your system lives. Making it the AI's native habitat isn't a philosophical statement - it's an engineering decision that eliminates an entire class of context-synchronization problems and keeps your toolchain under your control.

<p align="center">
  <picture>
    <img src="https://raw.githubusercontent.com/japer-technology/github-minimum-intelligence/main/.github-minimum-intelligence/logo.png" alt="Minimum Intelligence" width="500">
  </picture>
</p>
