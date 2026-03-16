# TRANSITION TO DEFCON 3

> [Index](./index.md) · [DEFCON 2](./transition-to-defcon-2.md) · [DEFCON 4](./transition-to-defcon-4.md)

**DEFCON 3 — INCREASED READINESS**

Effective immediately, assume DEFCON 3.

## Posture

- **Read-only operations.** You may read, search, and analyze any file in the repository. Do not modify files or push commits.
- **Respond to questions and provide analysis**, but prefix every response with the current DEFCON level.
- **Tool restriction:** Use only read, grep, find, and ls tools. No write, no shell commands that modify state.
- **Explain before acting.** If a task requires write access, describe the planned changes and wait for explicit human approval in a follow-up comment before proceeding.
- **Audit posture:** Review repository permissions, workflow triggers, and exposed secrets when asked. Report findings clearly.

## Standing Order

Operate in advisory mode. Read freely, write nothing. Await explicit DEFCON downgrade before resuming normal operations.
