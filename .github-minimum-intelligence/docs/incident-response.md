# 13. Incident Response Plan

> [Index](./index.md) · [Security Assessment](./security-assessment.md) · [Capabilities Analysis](./warning-blast-radius.md)
>
> **Classification:** Internal — For Repository Maintainers and Organization Administrators
>
> **Companion Document:** [security-assessment.md](./security-assessment.md) · [warning-blast-radius.md](./warning-blast-radius.md) · [transition-to-defcon-1.md](./transition-to-defcon-1.md)

---

## Purpose

This document provides precise, step-by-step procedures for **taking control** of a security incident involving the `github-minimum-intelligence` (GMI) agent. It covers containment, manual file deletion of compromised artifacts, disabling the workflow agent, and stopping any existing GitHub Actions runs.

**Use this plan when:**

- You suspect the agent has been compromised or is behaving unexpectedly.
- Unauthorized commits, branches, or workflow files have appeared.
- Secrets may have been exfiltrated.
- The agent is running autonomously and must be stopped immediately.

---

## Step 1: Stop Any Existing Actions

**Objective:** Immediately cancel all running and queued GitHub Actions workflow runs.

**Time target:** Minutes 0–2

### 1.1 Cancel via GitHub UI

1. Navigate to the repository **Actions** tab.
2. For **every** workflow run with status `In progress` or `Queued`:
   - Click the run to open it.
   - Click **Cancel workflow run** (top right).
3. Repeat for **all 24 organization repositories** if cross-repo compromise is suspected.

### 1.2 Cancel via GitHub CLI

```bash
# Cancel all in-progress runs for this repository
gh run list --status in_progress --json databaseId --jq '.[].databaseId' | \
  xargs -I {} gh run cancel {}

# Cancel all queued runs
gh run list --status queued --json databaseId --jq '.[].databaseId' | \
  xargs -I {} gh run cancel {}
```

### 1.3 Cancel across the organization

```bash
# For every repository in the organization
for repo in $(gh repo list japer-technology --json name --jq '.[].name'); do
  echo "Cancelling runs in $repo..."
  gh run list --repo "japer-technology/$repo" --status in_progress \
    --json databaseId --jq '.[].databaseId' | \
    xargs -I {} gh run cancel {} --repo "japer-technology/$repo"
done
```

### 1.4 Disable the workflow

```bash
# Disable the agent workflow so no new runs can start
gh workflow disable "github-minimum-intelligence-agent.yml"
```

> **Verification:** Confirm under **Actions → github-minimum-intelligence-agent** that the badge reads "This workflow is disabled" and no runs are in progress.

---

## Step 2: Take Control — Contain the Incident

**Objective:** Prevent further damage by isolating credentials, access, and the agent runtime.

**Time target:** Minutes 2–10

### 2.1 Rotate all secrets immediately

| Secret | Where to rotate | Command / Location |
|--------|-----------------|--------------------|
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/) | Regenerate the key and update the repo secret |
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com/) | Regenerate if configured |
| `GITHUB_TOKEN` | Auto-expires when the workflow ends | Verify no persistent tokens were created |
| `APP_PRIVATE_KEY` | GitHub App settings → Keys | Regenerate the private key |
| Any other provider keys | Respective provider consoles | Rotate and update repo secrets |

```bash
# Update a repository secret (after rotating the value at the provider)
gh secret set ANTHROPIC_API_KEY --body "sk-new-rotated-key-value"
```

### 2.2 Restrict repository access

1. **Enable branch protection** on `main` (if not already):
   - Require pull request reviews before merging.
   - Require status checks to pass.
   - Restrict who can push directly.
2. **Audit collaborator list:** Remove any unexpected users or pending invitations.
3. **Review GitHub App installations:** Revoke any unrecognised App installations on the repository.

### 2.3 Transition to DEFCON 1

If the agent is still accepting issue-triggered commands, open an issue containing the contents of [transition-to-defcon-1.md](./transition-to-defcon-1.md) to instruct it to **cease all autonomous operations**.

> **Note:** DEFCON 1 is a software-level instruction. It is not a substitute for disabling the workflow (Step 1.4). Always disable the workflow first.

---

## Step 3: Manual File Deletion — Eradicate Compromised Artifacts

**Objective:** Remove any files the agent created or modified without authorisation.

**Time target:** Minutes 10–60

### 3.1 Identify unauthorized changes

```bash
# Review recent commits (last 24 hours)
git log --all --oneline --since="24 hours ago"

# Show files changed in the last N commits
git diff --name-only HEAD~10

# Find new or modified workflow files
find .github/workflows -type f -newer security-assessment.md -ls

# Find new or modified files in the agent directory
find .github-minimum-intelligence -type f -newer security-assessment.md -ls
```

### 3.2 Delete unauthorized workflow files

If the agent injected new workflow files:

```bash
# Delete the specific unauthorized workflow file
git rm .github/workflows/<unauthorized-workflow>.yml

# Commit the deletion
git commit -m "incident: remove unauthorized workflow file"
git push origin main
```

### 3.3 Delete unauthorized branches

```bash
# List all remote branches
git branch -r

# Delete each unauthorized branch
git push origin --delete <unauthorized-branch-name>
```

### 3.4 Revert unauthorized commits

```bash
# Revert a specific commit (creates a new commit that undoes the changes)
git revert <commit-hash> --no-edit
git push origin main
```

### 3.5 Clean agent state files

If agent session or state files have been tampered with:

```bash
# Remove all agent state (conversations and issue mappings)
git rm -r .github-minimum-intelligence/state/sessions/*
git rm -r .github-minimum-intelligence/state/issues/*
git commit -m "incident: purge agent state files"
git push origin main
```

### 3.6 Repeat across all organization repositories

If cross-repository contamination is suspected, repeat steps 3.1–3.5 for every repository in the organization:

```bash
for repo in $(gh repo list japer-technology --json name --jq '.[].name'); do
  echo "Auditing $repo..."
  gh repo clone "japer-technology/$repo" "/tmp/$repo" -- --depth=50
  cd "/tmp/$repo"
  git log --all --oneline --since="24 hours ago"
  cd -
done
```

---

## Step 4: The Workflow Agent — Disable, Audit, and Rebuild

**Objective:** Ensure the agent workflow is safe before any re-enablement.

**Time target:** Hours 1–24

### 4.1 Audit the workflow file

Compare the current workflow against the known-good version:

```bash
# Diff the installed workflow against the upstream template
diff .github/workflows/github-minimum-intelligence-agent.yml \
     .github-minimum-intelligence/install/github-minimum-intelligence-agent.yml
```

Verify:
- [ ] The `authorization` step still checks collaborator permissions.
- [ ] No unexpected `schedule:`, `workflow_dispatch:`, or `push:` triggers have been added.
- [ ] No additional steps, jobs, or scripts have been injected.
- [ ] Environment variables and secrets match the expected set.

### 4.2 Audit the agent code

```bash
# Check for modifications to lifecycle scripts
git diff HEAD~20 -- .github-minimum-intelligence/lifecycle/
git diff HEAD~20 -- .github-minimum-intelligence/.pi/
```

Verify:
- [ ] `agent.ts` has not been modified to bypass safety checks.
- [ ] `APPEND_SYSTEM.md` has not been altered with malicious instructions.
- [ ] No new skills have been added to `.pi/skills/` without authorisation.

### 4.3 Re-enable with safeguards

Before re-enabling the workflow, implement the recommendations from [security-assessment.md Section 12](./security-assessment.md#12-recommendations):

1. **Restrict token scope:** Use a fine-grained personal access token scoped to this repository only.
2. **Enable branch protection:** Require pull request reviews for all changes.
3. **Add network egress controls:** Consider a self-hosted runner with firewall rules.
4. **Add a command allowlist:** Restrict the agent to read-only tools if appropriate.

```bash
# Re-enable the workflow only after all safeguards are in place
gh workflow enable "github-minimum-intelligence-agent.yml"
```

---

## Step 5: Recover and Communicate

**Objective:** Restore normal operations and inform stakeholders.

**Time target:** Hours 2–48

### 5.1 Validate repository integrity

```bash
# Verify no unexpected files remain
git status
find . -name '*.yml' -path '*/.github/workflows/*' -exec echo "Workflow: {}" \;

# Verify secrets are rotated
gh secret list
```

### 5.2 Notify stakeholders

| Audience | Channel | Content |
|----------|---------|---------|
| Organization admins | Direct message / email | Full incident timeline, actions taken, remaining risks |
| Repository contributors | GitHub Issue (private repo) or direct contact | Summary of what happened, what was affected, what action they need to take |
| Downstream consumers | Advisory / release note | Whether shipped code was affected, recommended actions |
| LLM provider (Anthropic, etc.) | Support channel | Key rotation confirmation, request for usage audit |
| GitHub Support | Support ticket | If org-wide token abuse is suspected |

### 5.3 Document the incident

Create an incident record capturing:
- **Timeline:** When the incident was detected, contained, eradicated, and resolved.
- **Root cause:** How the compromise occurred (prompt injection, compromised account, etc.).
- **Blast radius:** Which repositories, secrets, and systems were affected.
- **Actions taken:** Every step performed during response.
- **Lessons learned:** What controls failed and what will be improved.

---

## Step 6: Learn and Harden

**Objective:** Prevent recurrence.

**Time target:** Days 1–7

- [ ] Conduct a post-incident review with all involved parties.
- [ ] Update the threat model in [security-assessment.md](./security-assessment.md) with new attack vectors discovered.
- [ ] Implement additional monitoring (e.g., alerts on workflow file changes, unexpected branch creation).
- [ ] Review and tighten permissions across all organization repositories.
- [ ] Consider moving to a self-hosted runner with network restrictions and reduced privileges.
- [ ] Update this incident response plan with any new procedures identified.
- [ ] Share findings with the broader community to help others avoid similar incidents.

---

## Quick Reference Card

```
┌────────────────────────────────────────────────────────────────┐
│                INCIDENT RESPONSE — QUICK REFERENCE             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. STOP ACTIONS      gh run cancel, gh workflow disable       │
│  2. TAKE CONTROL      Rotate secrets, lock down access         │
│  3. DELETE FILES      git rm, git revert, delete branches      │
│  4. AUDIT THE AGENT   Diff workflow & lifecycle files          │
│  5. RECOVER           Validate, notify, document               │
│  6. HARDEN            Post-incident review, implement fixes    │
│                                                                │
│  Emergency:  git revert <hash>, then think.                    │
│  DEFCON 1:   See transition-to-defcon-1.md                     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

*This incident response plan is maintained under the obligations of the Third Law (Preserve Integrity). Preparedness is not paranoia — it is a duty.*
