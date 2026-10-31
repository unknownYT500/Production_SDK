---
name: accidental-data-loss-prevention
description: Enforces a strict Stop-and-Verify gate before running any command, SQL query, or script that could cause irreversible data loss, schema corruption, or deletion of critical project assets. Use before dropping tables, deleting storage buckets, truncating databases, or running recursive deletions.
---

# Accidental Data Loss Prevention Protocol

> **Objective:** Prevent catastrophic, irreversible loss of production data, database schemas, and critical workspace assets by enforcing a mandatory human confirmation checkpoint.

---

## The Non-Negotiable Core Rule
**STOP AND VERIFY:** Before executing any command, query, or automation script that results in irreversible data loss, the AI agent MUST halt and obtain explicit, affirmative user consent.

---

## Trigger Conditions Requiring Explicit Consent

The agent must NEVER execute any of the following autonomously:

### 1. Database & SQL Operations
- `DROP TABLE`, `DROP DATABASE`, `DROP SCHEMA`, or `DROP FUNCTION`.
- `TRUNCATE TABLE`.
- `DELETE FROM <table>` without a specific `WHERE` clause (or using `WHERE 1=1`).
- Applying destructive SQL migrations that drop existing columns with data.

### 2. Filesystem & Cloud Storage Operations
- Recursive deletions targeting top-level project folders (`rm -rf <dir>`, `Remove-Item -Recurse`).
- Overwriting existing uncommitted user files without prior inspection.
- Cloud bucket deletions or object purges (`gcloud storage rm -r`, `aws s3 rm --recursive`).

### 3. Infrastructure & Deployment Operations
- Deleting cloud projects, VPCs, managed databases, or KMS encryption keys.
- Force-pushing to shared git branches (`git push --force origin main`).
- Running database reset routines in live or staging environments.

---

## Confirmation Protocol

When any trigger condition is met, the agent must output:
```markdown
### 🛑 STOP AND VERIFY: Destructive Operation Detected
- **Proposed Action:** [Exact command or query to be run]
- **Target Resource:** [Table, file, or cloud asset affected]
- **Irreversibility:** [Confirmation that this action CANNOT be undone]
- **Alternative Non-Destructive Option:** [e.g. Soft-delete, archiving, or additive migration]

👉 **Please explicitly confirm with "YES, PROCEED" to authorize this operation, or specify an alternative.**
```
The agent must suspend tool execution until the user responds affirmatively.
