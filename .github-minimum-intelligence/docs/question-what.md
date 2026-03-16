# Question: What?

> [Index](./index.md) · [Questions Overview](./questions.md) · [The Repo Is the Mind](./the-repo-is-the-mind.md)

## What is GitHub Minimum Intelligence?

Most AI coding products answer the question *“what is this?”* with deployment vocabulary: platform, workspace, cloud memory, seat management, integration tier. GitHub Minimum Intelligence answers differently. It is not a destination you move your work into. It is a pattern you drop into the place your work already lives: the repository.

That seemingly small shift changes almost everything.

If a traditional AI assistant is an external service that occasionally touches your codebase, Minimum Intelligence is a **local intelligence layer** that derives its capabilities from the repository’s existing primitives—issues, workflows, markdown, commits, and permissions. In other words, it is less “new product category” and more “recomposition of tools you already trust.”

---

## What it is, in strict technical terms

At its core, the system is composed of:

- a repo-local folder (`.github-minimum-intelligence`) containing prompts, workflow logic, state conventions, and behavior files,
- a workflow runtime (GitHub Actions) that executes the agent loop,
- an LLM provider key you supply,
- and a set of committed artifacts that preserve conversation and behavioral history.

The project description in this repository is explicit: the agent *lives in your GitHub repo*, responds to issues, remembers conversations, and commits its work. That definition is not metaphorical branding; it is an implementation detail reflected in file layout and workflow behavior.

So when we ask **what** Minimum Intelligence is, the most accurate answer is:

> It is an installation model for repository-embedded agency, where AI behavior is expressed as versioned configuration and AI memory is persisted as source-controlled state.

That sentence sounds abstract, but every part maps to concrete developer mechanics: open issue, trigger workflow, run agent, produce commit, persist transcript.

---

## What it is not

The clarity of this project comes from what it deliberately refuses to be.

It is not:

- a hosted IDE,
- a vendor-owned conversational silo,
- a separate memory database you cannot inspect,
- a proprietary “agent operating system” that bypasses Git controls,
- or a dashboard-first workflow that treats your repository as a synchronization target.

Instead, it accepts a strict constraint: intelligence must be legible through normal repository operations. If something matters, it should exist as files, commits, comments, or workflow definitions.

This is why “minimum” is a meaningful adjective here. It does not signal weak capability. It signals **minimal additional infrastructure**.

---

## What problem class it actually solves

Many discussions frame AI coding tools as generation engines (“how well does it write code?”). Minimum Intelligence reframes the core failure mode as **context discontinuity**.

Developers do not merely need text completion; they need continuity of intent:

- Why this architecture and not the obvious alternative?
- What constraints were non-negotiable last month?
- Which prior decisions are policy, and which were temporary compromises?

Conventional chat tools leak this continuity because conversation memory lives outside delivery systems. Here, memory lives alongside delivery systems. State is represented in repository artifacts and recoverable by standard Git operations.

So the “what” is not just an agent; it is a **continuity mechanism** for software teams who already coordinate through GitHub.

---

## What the repository becomes under this model

Minimum Intelligence effectively upgrades the semantic role of the repo.

Traditionally, a repository is treated as:

1. source-of-truth for code,
2. event log for changes,
3. collaboration surface for review.

Under this pattern, it becomes a fourth thing:

4. **runtime-adjacent memory substrate for machine collaboration**.

That sounds grand, but it is practical. The same primitives that make human collaboration durable—history, diff, attribution, branch governance—become the exact mechanisms by which AI collaboration remains governable.

The repository stops being “where code ends up” and becomes “where reasoning accumulates.”

---

## What kind of trust model this implies

AI trust is often discussed as model quality, but in engineering organizations trust is mostly procedural:

- Can we inspect what happened?
- Can we reproduce it?
- Can we limit who can trigger it?
- Can we revert bad outcomes?

Minimum Intelligence inherits answers from GitHub itself. Permissions are repository permissions. Review is pull request review. Rollback is git revert. History is commit history.

This is a profound simplification. Rather than introducing new governance machinery, the project piggybacks on existing governance machinery. The result is a lower cognitive burden for adoption, especially for teams with compliance or audit requirements.

---

## What “agent identity” means here

One of the most subtle parts of the design is that the agent’s persona and behavioral boundaries are stored as editable files. That means identity is not a hidden server-side preset but a versioned artifact.

In practice, this creates a new operational capability: teams can review and evolve AI behavior through the same pull-based process they use for code. Personality, style, risk posture, and instruction hierarchy become inspectable policy text.

So what is the agent? Not an immutable assistant instance. It is a **maintained configuration surface** whose behavior can be iterated deliberately.

---

## What makes this more than “just automation”

A skeptic might say: “Isn’t this just a workflow bot with an LLM call?”

Technically, yes—and that is precisely why it matters.

Great infrastructure patterns often look obvious in hindsight because they compose familiar parts rather than requiring exotic systems. Minimum Intelligence is powerful for the same reason Git itself was powerful: it changes reliability and collaboration properties by changing *where state lives* and *how history is recorded*.

The value is not magic cognition alone; it is cognition coupled to durable, reviewable, revertible process.

---

## What this suggests for the future

If this model generalizes, we should expect an ecosystem where:

- repositories ship with first-class AI constitutions,
- issue threads double as executable planning surfaces,
- organization policy is encoded into agent behavior files,
- and model choice becomes a swappable dependency rather than a platform lock-in decision.

In that future, “using AI for software” will feel less like consulting an oracle and more like collaborating with a junior-to-senior teammate whose memory is literally your commit graph.

---

## Final answer: what is it?

GitHub Minimum Intelligence is a repository-native AI collaboration framework.

It is **not** primarily a chatbot, nor primarily a platform. It is a disciplined way to bind LLM reasoning to the software delivery substrate teams already operate.

Its core claim is simple and radical:

- put intelligence inside the repo,
- keep memory in git,
- keep identity in files,
- keep execution in workflows,
- keep control with the maintainers.

When those conditions hold, AI stops being an external convenience layer and becomes an internal, governable part of engineering practice.
