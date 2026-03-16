# Dependencies

> No repo is an island.
> Every codebase depends on memory, intent, and shared understanding

## Direct Dependencies

### Runtime (npm)

| Package | Version | Description |
|---------|---------|-------------|
| [@mariozechner/pi-coding-agent](https://github.com/badlogic/pi-mono) | 0.57.1 | Coding agent CLI with read, bash, edit, and write tools and session management. This is the core AI agent that powers the entire Minimum Intelligence system - it processes prompts, interacts with LLM providers, and manages conversation sessions. |

### pi-mono Feature Surface

Beyond the CLI binary, GMI uses the following pi-mono feature categories:

| Feature | Location | Description |
|---------|----------|-------------|
| Session management | `--session-dir`, `--session` | Multi-turn conversation continuity across workflow runs |
| Project settings | `.pi/settings.json` | Provider, model, thinking level, compaction, and retry configuration |
| System prompt extension | `.pi/APPEND_SYSTEM.md` | Behavioural guidelines appended to the default system prompt |
| Bootstrap protocol | `.pi/BOOTSTRAP.md` | First-run agent identity setup |
| Context files | `AGENTS.md` | Project-specific instructions loaded at startup |
| Skills | `.pi/skills/` | On-demand capability packages (`memory`, `skill-creator`) |
| Prompt templates | `.pi/prompts/` | Reusable prompts for recurring workflows (`code-review`, `issue-triage`) |
| Extensions | `.pi/extensions/` | Custom tools registered for LLM use (`github_repo_context`) |

See [docs/analysis/pi-mono-feature-utilization.md](docs/analysis/pi-mono-feature-utilization.md) for a full audit of used vs. available features.

## Infrastructure Dependencies

These are not package dependencies but are required for the system to function:

| Dependency | Description |
|------------|-------------|
| [GitHub Actions](https://github.com/features/actions) | The sole compute runtime. Every issue event triggers a workflow that runs the AI agent. No external servers or containers are needed. |
| [GitHub Issues](https://docs.github.com/en/issues) | Used as the conversation interface. Each issue maps to a persistent AI conversation thread. |
| [Git](https://git-scm.com/) | All session state, conversation history, and agent edits are committed to the repository. Git serves as the memory and storage layer. |
| [Bun](https://bun.sh) | JavaScript/TypeScript runtime used to execute the agent orchestrator and install dependencies. |
| [gh CLI](https://cli.github.com/) | GitHub's official CLI tool, used by the agent lifecycle scripts to interact with the GitHub API (fetching issues, posting comments, managing reactions). |

## GitHub Actions Workflow Dependencies

These are referenced in `.github/workflows/`:

| Action | Workflow | Description |
|--------|----------|-------------|
| [actions/checkout@v6](https://github.com/actions/checkout) | agent | Checks out the repository so the agent can read and write files. |
| [oven-sh/setup-bun@v2](https://github.com/oven-sh/setup-bun) | agent | Installs the Bun runtime in the GitHub Actions environment. |
| [actions/cache@v5](https://github.com/actions/cache) | agent | Caches `node_modules` keyed on the `bun.lock` hash to speed up dependency installation. |
| [actions/configure-pages@v5](https://github.com/actions/configure-pages) | agent | Configures GitHub Pages deployment (auto-enables Pages when the repo is used as a template). |
| [actions/upload-pages-artifact@v4](https://github.com/actions/upload-pages-artifact) | agent | Uploads the static site artifact from `.github-minimum-intelligence/public-fabric/`. |
| [actions/deploy-pages@v4](https://github.com/actions/deploy-pages) | agent | Deploys the uploaded artifact to GitHub Pages. |

## LLM Provider Dependencies (one required)

An API key from at least one supported LLM provider is needed:

| Provider | API Key Secret | Description |
|----------|---------------|-------------|
| [OpenAI](https://platform.openai.com/) | `OPENAI_API_KEY` | GPT models including GPT-5.4 (default provider). |
| [Anthropic](https://console.anthropic.com/) | `ANTHROPIC_API_KEY` | Claude models. |
| [Google Gemini](https://aistudio.google.com/) | `GEMINI_API_KEY` | Gemini 2.5 Pro and Flash models. |
| [xAI](https://console.x.ai/) | `XAI_API_KEY` | Grok 3 and Grok 3 Mini models. |
| [OpenRouter](https://openrouter.ai/) | `OPENROUTER_API_KEY` | Access to DeepSeek, and hundreds of other models via a unified API. |
| [Mistral](https://console.mistral.ai/) | `MISTRAL_API_KEY` | Mistral Large and other Mistral models. |
| [Groq](https://console.groq.com/) | `GROQ_API_KEY` | Fast inference for open-source models like DeepSeek R1 distills. |

## Transitive Dependencies (notable)

These are pulled in transitively by `@mariozechner/pi-coding-agent`:

| Package | Description |
|---------|-------------|
| `@anthropic-ai/sdk` | Official Anthropic API client for Claude models. |
| `@aws-sdk/client-bedrock-runtime` | AWS Bedrock client for accessing models via AWS infrastructure. |
| `openai` | Official OpenAI API client. |
| `@google/genai` | Google's Generative AI SDK for Gemini models. |
| `fast-xml-parser` | Fast XML parser used by AWS SDK internals. |
| `tslib` | TypeScript runtime helpers used throughout the dependency tree. |

<p align="center">
  <picture>
    <img src="https://raw.githubusercontent.com/japer-technology/github-minimum-intelligence/main/.github-minimum-intelligence/logo.png" alt="Minimum Intelligence" width="500">
  </picture>
</p>
