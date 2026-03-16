import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";

/**
 * GitHub Context Extension
 *
 * Provides a structured tool for retrieving repository metadata so the LLM
 * does not need to construct `gh` CLI invocations from memory.
 */
export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "github_repo_context",
    label: "GitHub Repository Context",
    description:
      "Returns structured metadata about the current GitHub repository: " +
      "name, description, default branch, visibility, topics, and language. " +
      "Use this when you need to understand the repository you are working in.",
    parameters: Type.Object({}),
    async execute(_toolCallId, _params, _signal) {
      try {
        const { execSync } = await import("node:child_process");
        const raw = execSync(
          "gh repo view --json name,description,defaultBranchRef,visibility,repositoryTopics,primaryLanguage",
          { encoding: "utf-8", timeout: 15_000 },
        );
        const repo = JSON.parse(raw);
        const result = {
          name: repo.name ?? "",
          description: repo.description ?? "",
          defaultBranch: repo.defaultBranchRef?.name ?? "main",
          visibility: repo.visibility ?? "unknown",
          topics: (repo.repositoryTopics ?? []).map(
            (t: { name: string }) => t.name,
          ),
          primaryLanguage: repo.primaryLanguage?.name ?? "unknown",
        };
        return {
          content: [{ type: "text" as const, text: JSON.stringify(result, null, 2) }],
          details: {},
        };
      } catch (err) {
        const message =
          err instanceof Error ? err.message : String(err);
        return {
          content: [
            {
              type: "text" as const,
              text: `Failed to retrieve repository context: ${message}. Ensure gh CLI is authenticated and you are in a GitHub repository.`,
            },
          ],
          details: {},
        };
      }
    },
  });
}
