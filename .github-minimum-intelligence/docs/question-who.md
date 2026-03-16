# Question: Who?

> [Index](./index.md) · [Questions Overview](./questions.md) · [The Repo Is the Mind](./the-repo-is-the-mind.md)

## Who is the "mind" when the repository becomes intelligent?

If *[The Repo Is the Mind](the-repo-is-the-mind.md)* asks us to relocate intelligence from an external platform into the repository, then the natural follow-up is not merely technical. It is existential: **who is acting when work is done?**

In most software systems, that question is easy. A person authors code, a bot runs checks, and infrastructure executes automation. Minimum Intelligence deliberately blurs those boundaries—but in a disciplined way. It does not pretend the agent is human, and it does not treat humans as interchangeable with automation. Instead, it introduces a new participant in the development process: a repository-native actor whose identity, memory, and authority are all governed by the same artifacts developers already trust.

"Who" in this architecture is not a single being. It is a layered identity stack.

---

## 1) Who speaks? The issue author starts the conversation.

The first voice in this system is still human. The repository collaborator opens an issue, leaves a comment, asks a question, or requests a change. The README frames this directly: issues are not ticket metadata around the work; they *are* the conversational interface for the agent lifecycle.

That means the initiating "who" is visible, permissioned, and socially legible. It is the same person identity model your team already uses for code review and contribution. No parallel account system, no separate chatbot workspace, no shadow identity layer.

In practical terms, the human does not step outside the project to talk to an assistant. They speak from inside the project, using the project's own social substrate.

---

## 2) Who executes? The workflow is the body.

Once a comment lands, GitHub Actions becomes the agent's body. This is one of the deepest ideas in the repo: the intelligence may be model-driven, but action is workflow-driven.

The agent does not wave hands over your codebase through a remote API. It runs in CI, in a checked-out worktree, with explicit repository-scoped permissions. In that sense, the workflow file is the anatomy of agency: what can be read, what can be written, which events can trigger behavior, and which credentials are in scope.

So, if we ask "who changed the code?" the answer is nuanced but precise:
- a human requested work,
- an LLM reasoned,
- and the workflow—under declared permissions—performed concrete operations.

Minimum Intelligence clarifies that execution authority is infrastructural, not mystical.

---

## 3) Who remembers? Git is the continuity layer.

Conventional assistants are often amnesiac because memory belongs to vendor sessions. This repository inverts that model. It binds conversation continuity to files under version control and stable issue mappings.

That means "who remembers" is not an always-on black box. It is the repository itself:
- issue threads preserve conversational intent,
- state files preserve session linkage,
- commits preserve behavioral effects.

Identity, then, becomes historical rather than purely instantaneous. The agent at time *t* is defined not only by prompt instructions at HEAD, but by the accumulated trace of interactions and edits. In human terms, this is character through history, not persona through branding.

---

## 4) Who decides what kind of agent this is? Maintainers, in Markdown.

The `Who` section in *[The Repo Is the Mind](the-repo-is-the-mind.md)* is explicit: agent identity is checked-in configuration. Persona is authored through dialogue, stored in repository files, and changed through ordinary Git operations.

This matters because it relocates authorship of behavior. The agent is not "who the vendor says it is". It is who the maintainers define it to be:
- tone can be adjusted,
- priorities can be reweighted,
- constraints can be tightened,
- and every change can be reviewed, blamed, reverted, or branched.

That is a profoundly different answer to "who is this assistant?" It is: **the assistant your repo has specified, at this commit, under this governance.**

---

## 5) Who has power? Permissions, not vibes.

The `app-manifest.json` reveals a core truth often hidden in AI tooling marketing: agency is bounded by permission scopes and event subscriptions. Issues, contents, actions, metadata; issue and installation events—these are not implementation footnotes. They are the constitutional limits of the actor.

In other words, identity in this system is inseparable from authority. "Who" is never just personality. "Who" is what token can do.

Minimum Intelligence is strongest where it is least romantic: it maps power to explicit config, and config to repository ownership. This is why the model can be swappable, the package can be pinned, and behavior can remain under local control.

---

## 6) Who is accountable? Everyone, with different surfaces.

The architecture distributes accountability instead of obscuring it.

- **Maintainers** are accountable for instructions, workflow design, and permission boundaries.
- **Contributors** are accountable for requests they make and reviews they approve.
- **The agent process** is accountable through artifacts: comments, diffs, commits, logs.
- **The model provider** is accountable for reasoning quality but cannot silently rewrite local governance.

This is why "[The Repo Is the Mind](the-repo-is-the-mind.md)" feels less like a metaphor and more like an operational doctrine. The repository already hosts accountability mechanisms—history, diff, review, rollback. Embedding the agent there means those mechanisms apply by default.

---

## 7) Who are "we" after adoption?

Perhaps the most interesting shift is collective identity. Teams using this pattern gradually stop treating AI as an external oracle and start treating it as a project participant with bounded agency.

"We" becomes:
- humans who define goals,
- automation that enforces process,
- and a model-guided worker that translates language into repository actions.

Not one of these replaces the others. The system works because each layer is explicit.

And that may be the real contribution of this repo: it refuses the false choice between "AI does everything" and "AI is just autocomplete." It proposes a third posture—**AI as a governed collaborator inside version control reality.**

---

## Closing: The answer to WHO is a commit, not a slogan.

Who is the mind?

At any given moment: the current tree, the current history, the current instructions, the current permissions, and the current conversation.

That answer is refreshingly untheatrical. It does not depend on anthropomorphism. It depends on artifacts.

In Minimum Intelligence, identity is not hidden in a proprietary backend. It is staged, negotiated, and persisted in the same medium as software itself. The repository does not merely *contain* intelligence. It defines who that intelligence is allowed to become.
