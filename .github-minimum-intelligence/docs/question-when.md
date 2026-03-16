# Question: When?

> [Index](./index.md) · [Questions Overview](./questions.md) · [The Repo Is the Mind](./the-repo-is-the-mind.md)

## The Temporal Architecture of Repository-Native Intelligence

The most underestimated word in software is not *what*, *how*, or even *why*. It is *when*.

In conventional AI tooling, *when* is an accident: whatever fits inside the current session, whatever survived copy-paste, whatever a model can infer from your latest prompt. In **Minimum Intelligence**, *when* is engineered. Time is not an emergent side effect of chat history; it is an explicit design primitive anchored to Git commits, issue threads, and workflow runs.

That distinction changes everything.

---

## 1) When Memory Stops Being Ephemeral

Most AI-assisted development systems behave like brilliant amnesiacs. They can reason, summarize, and generate code—yet each interaction begins with a hidden tax: reconstructing context. You re-explain architecture, repeat old constraints, and restate decisions you already made last week.

The repository-native model rejects this waste. Here, continuity does not depend on model RAM or a vendor-held transcript. It depends on durable artifacts:

- Issue threads for conversational intent
- Git history for executed decisions
- Repository files for present truth
- Workflow logs for runtime evidence

In this design, “later” is no longer a weaker version of “now.” A response next month can be richer than a response today, because more evidence exists in the record.

---

## 2) When Becomes a First-Class Constraint

*[The Repo Is the Mind](the-repo-is-the-mind.md)* frames the agent as stateless per invocation, stateful across history. That is a precise and powerful asymmetry.

- **Stateless execution** protects reliability: each run is fresh, deterministic, and reconstructible.
- **Stateful history** protects continuity: each run inherits durable context from Git and Issues.

This means the system is not pretending to be a persistent consciousness. Instead, it becomes something more useful in engineering terms: a process that can always reboot without forgetting institutional memory.

If classic chatbots are “ongoing conversations,” Minimum Intelligence is “ongoing evidence.”

---

## 3) When Trust Is Auditable

There is a practical reason this temporal model matters: trust decays when memory is private.

In hosted AI workflows, the timeline lives somewhere else. You cannot `git blame` a prompt. You cannot branch a personality tweak. You cannot inspect a historical state transition with the same primitives you use for code review.

Minimum Intelligence collapses those boundaries:

- Persona is checked-in configuration.
- Session state is committed.
- Outputs are diffs.
- Decisions are replayable.

So “when did the agent start doing this?” gets the same answer as any software question: find the commit.

Temporal accountability is not added on top; it is the substrate.

---

## 4) When Collaboration Stops Resetting to Zero

The hardest collaboration problem in AI coding is not correctness—it is re-entry.

Humans work asynchronously: meetings interrupt us, priorities shift, branches diverge, people disappear for weeks and return. A useful agent must survive this rhythm.

Repository-native intelligence does because it binds conversations to issue numbers and state files, then rehydrates context at execution time. There is no mystical “session continuity” to preserve. There is only durable project memory to query.

The result is profound in mundane ways:

- You can pause a thread for a month and resume without ritual recap.
- You can onboard a new maintainer and show a factual trail, not a narrative summary.
- You can evolve requirements in public, with diffs recording every pivot.

The agent does not merely answer in time. It answers *across time*.

---

## 5) When Infrastructure Is Philosophy

The repo’s architecture quietly encodes a philosophy: sovereignty over convenience.

Choosing GitHub Actions as runtime, Git as memory, and Markdown/YAML as configuration is not just implementation detail. It is a decision about where intelligence should live.

- Not in proprietary conversation silos
- Not behind opaque orchestration
- Not in undocumented prompt layers

But in plain files, versioned history, and standard developer tooling.

This turns *when* into governance. If time is stored in your own artifacts, your organization—not a vendor dashboard—defines retention, visibility, and review.

---

## 6) When the Repository Becomes Cognitive Terrain

A repository has always stored more than code. It stores arguments, experiments, reversions, dead ends, and recovered intent. Minimum Intelligence simply treats this as computationally meaningful.

That is the central move:

> The repo is not a destination for AI output. It is the medium in which AI thought becomes accountable.

Once you accept that, *when* stops being a scheduling question and becomes an epistemic one:

- **When is a decision valid?** When it is visible in context.
- **When is memory reliable?** When it is durable and inspectable.
- **When is collaboration real?** When future contributors can replay the reasoning, not just read the result.

---

## 7) When, Finally, Is the Right Time?

The usual answer is: when models get better, when tooling matures, when agents become more autonomous.

The better answer this repository offers is simpler:

**Now—if you are willing to treat history as infrastructure.**

Because the key breakthrough is not bigger context windows or cleverer prompts. It is putting cognition inside the same system that already manages your source of truth.

Code learned this lesson decades ago: version everything that matters.

Minimum Intelligence extends the rule:

Version the conversation.
Version the constraints.
Version the persona.
Version the memory.

Then “when” ceases to be a fear—of forgetting, drifting, or losing control—and becomes a capability: the ability to reason faithfully with your past while building your future.

---

In that sense, the most important clock in AI-assisted software is not wall time.

It is commit time.
