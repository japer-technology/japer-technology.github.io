# Contributing to GitHub Minimum Intelligence

Thank you for your interest in contributing. This project values transparency, auditability, and human judgment above all else. Every contribution — code, documentation, or discussion — becomes part of the repository's permanent history.

Before contributing, please read [Before You Begin](.github-minimum-intelligence/docs/final-warning.md) and the [Four Laws of AI](.github-minimum-intelligence/docs/the-four-laws-of-ai.md).

---

## How to Contribute

### Reporting Bugs

Open a [GitHub Issue](../../issues) with:

- A clear, descriptive title.
- Steps to reproduce the problem.
- What you expected to happen and what actually happened.
- Your environment (OS, Bun version, LLM provider).

### Suggesting Features

Open a [GitHub Issue](../../issues) describing:

- The problem or gap the feature addresses.
- How it fits within the existing architecture (issues as conversation, Git as memory, Actions as runtime).
- Any security implications — review the [Capabilities Analysis](.github-minimum-intelligence/docs/warning-blast-radius.md) to understand the access model.

### Submitting Changes

1. Fork the repository and create a branch from `main`.
2. Make your changes in small, reviewable increments.
3. Test locally with `cd .github-minimum-intelligence && bun install` and verify dependencies install cleanly.
4. Open a pull request with a clear description of what changed and why.

---

## Project Structure

```
.github-minimum-intelligence/       # Core agent framework
  .pi/                              # Agent personality, skills, and LLM config
  install/                          # Default templates for agent identity and settings
  lifecycle/                        # Agent orchestrator and runtime hooks
  state/                            # Git-tracked session history and issue mappings

.github/                            # GitHub Actions workflows and issue templates
```

See the [README](README.md#project-structure) for a detailed breakdown of every file.

---

## Development Setup

1. Install [Bun](https://bun.sh).
2. Clone the repository.
3. Install dependencies:
   ```bash
   cd .github-minimum-intelligence && bun install
   ```
4. Add an LLM API key as a repository secret (see [Supported Providers](README.md#supported-providers)).

---

## Style and Conventions

- **Documentation** is Markdown. Use tables, clear headings, and concise language consistent with existing files.
- **Code** is TypeScript, executed with Bun.
- **Skills** are self-contained Markdown files in `.github-minimum-intelligence/.pi/skills/`.
- **Commit messages** should be short and descriptive. Every commit is permanent and auditable.

---

## Security

If you discover a security vulnerability, **do not open a public issue**. Instead, refer to the [Incident Response](.github-minimum-intelligence/docs/incident-response.md) plan and contact the maintainers privately.

All contributions are subject to the project's [Security Assessment](.github-minimum-intelligence/docs/security-assessment.md) and [Capabilities Analysis](.github-minimum-intelligence/docs/warning-blast-radius.md). Changes that expand the agent's capabilities or permissions require careful review.

---

## Code of Conduct

All contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE.md).
