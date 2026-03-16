# Index

> Comprehensive guide to all GitHub Minimum Intelligence documentation.
>
> **Start here:** [README](../../README.md) · **Before You Begin:** [Important Information](./final-warning.md) · **Laws:** [The Four Laws of AI](./the-four-laws-of-ai.md)

---

## Core Project Documentation

| Document | Description |
|----------|-------------|
| [README](../../README.md) | Project overview, quick start, installation methods, configuration, and supported providers. |
| [CONTRIBUTING](../../CONTRIBUTING.md) | How to report bugs, suggest features, submit changes, and set up a development environment. |
| [CODE OF CONDUCT](../../CODE_OF_CONDUCT.md) | Community standards, expected behavior, and alignment with the Four Laws. |
| [LICENSE](../../LICENSE.md) | MIT License. |

---

## Safety & Governance

| Document | Description |
|----------|-------------|
| [Before You Begin](./final-warning.md) | Important usage information, precautions, side effects, and the complete governance framework. **Read this first.** |
| [The Four Laws of AI](./the-four-laws-of-ai.md) | The Zeroth, First, Second, and Third Laws governing all AI behavior in this system. |

---

## Security

| Document | Description |
|----------|-------------|
| [Security Assessment](./security-assessment.md) | Comprehensive security review covering threat model, vulnerability assessment, access control, supply chain, and compliance with the Four Laws. |
| [Capabilities Analysis](./warning-blast-radius.md) | Evidence-based audit of agent capabilities and access scope — code access, secret exposure, cross-repository access, and persistence mechanisms. |
| [Incident Response Plan](./incident-response.md) | Step-by-step procedures for containment, eradication, recovery, and hardening after a security incident. |

---

## DEFCON Readiness Levels

Operational readiness states that constrain agent behavior. Higher readiness (lower number) means tighter restrictions.

| Level | Document | Posture |
|-------|----------|---------|
| **DEFCON 1** | [Maximum Readiness](./transition-to-defcon-1.md) | All operations suspended. No file modifications, no tool use, no code execution. |
| **DEFCON 2** | [High Readiness](./transition-to-defcon-2.md) | Read-only, advisory only. No file modifications. |
| **DEFCON 3** | [Increased Readiness](./transition-to-defcon-3.md) | Read-only. Explain planned changes and await human approval. |
| **DEFCON 4** | [Above Normal Readiness](./transition-to-defcon-4.md) | Full capability with elevated discipline. Confirm intent before every write. |
| **DEFCON 5** | [Normal Readiness](./transition-to-defcon-5.md) | Standard operations. All capabilities available. |

---

## Foundational Questions

Six questions define the philosophical and architectural foundation of this project.

| Question | Document | Core Inquiry |
|----------|----------|--------------|
| **What?** | [question-what.md](./question-what.md) | What is GitHub Minimum Intelligence? A repository-native AI collaboration framework. |
| **Who?** | [question-who.md](./question-who.md) | Who speaks, executes, remembers, and governs when the repository becomes the mind? |
| **When?** | [question-when.md](./question-when.md) | How Git commits replace ephemeral sessions — memory becomes durable, trust becomes auditable. |
| **Where?** | [question-where.md](./question-where.md) | Where intelligence lives — runtime, memory, identity, and authorization. |
| **How?** | [question-how.md](./question-how.md) | Issues as input, Actions as runtime, LLM as reasoning, Git as memory. |
| **How Much?** | [question-how-much.md](./question-how-much.md) | How much intelligence can a repository hold? The ceiling is stewardship, not token count. |

**Overview:** [questions.md](./questions.md) · **Architectural thesis:** [The Repo Is the Mind](./the-repo-is-the-mind.md)

---

## Architecture

| Document | Description |
|----------|-------------|
| [The Repo Is the Mind](./the-repo-is-the-mind.md) | The architectural thesis — why the repository is the AI's natural habitat, covering What, Where, How, Who, When, and Why. |
| [Questions Overview](./questions.md) | Summary table of all six foundational questions. |

---

## Agent Configuration

| Document | Location | Description |
|----------|----------|-------------|
| [AGENTS.md](../AGENTS.md) | `.github-minimum-intelligence/` | Agent identity — name, personality, and behavioral guidance. |
| [PACKAGES.md](../PACKAGES.md) | `.github-minimum-intelligence/` | Runtime dependencies and required packages. |

---

## Related Links

- [Quick Start](../../README.md#quick-start) — Get running in under 5 minutes.
- [Installation Methods](../../README.md#installation-methods) — Setup script, manual copy, or GitHub App.
- [Supported Providers](../../README.md#supported-providers) — Anthropic, OpenAI, Google Gemini, xAI, DeepSeek, Mistral, Groq, OpenRouter.
- [Configuration](../../README.md#configuration) — Change models, adjust thinking level, filter by label.
- [Project Structure](../../README.md#project-structure) — Complete file layout.

---

<p align="center">
  <picture>
    <img src="https://raw.githubusercontent.com/japer-technology/github-minimum-intelligence/main/.github-minimum-intelligence/logo.png" alt="Minimum Intelligence" width="500">
  </picture>
</p>
