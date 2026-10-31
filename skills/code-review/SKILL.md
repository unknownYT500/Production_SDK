---
name: code-review
description: Evaluates proposed code changes against production standards, test coverage requirements, security policies, and architectural contracts before merging into main. Use before creating pull requests, during peer code reviews, or before deployment.
---

# Senior Engineer Code Review Protocol

> **Objective:** Catch architectural regressions, missing tests, security leaks, and code smells before code is merged into the authoritative branch.

---

## When to Use This Skill
- Reviewing a completed feature or bug fix before merging into `main`.
- Evaluating pull requests submitted by teammates or companion agents.
- Conducting pre-flight verification before releasing a production build.

---

## The 5-Point Code Review Rubric

Every code review must evaluate changes against these five gates:

### 1. Contract & Interface Stability
- Did the change modify public function signatures, API routes, or database columns?
- If yes, did it maintain backwards compatibility for existing clients (mobile apps, webhooks)?
- Are all new types and parameters fully typed (zero implicit `any`)?

### 2. Empirical Verification & Test Proof
- Does the PR include automated tests proving the new behavior works?
- If this is a bug fix, is there a regression test that reproduced the failure first?
- Did the test suite run, and did 100% of tests pass without skipped or commented-out assertions?

### 3. Security & Zero-Trust Hygiene
- Are there any exposed API keys, private keys, or passwords committed in the diff?
- Is all citizen/customer PII encrypted or hashed before database insertion?
- Are database operations guarded by Row-Level Security (RLS) policies?
- Are inputs validated using strict schemas (e.g., Zod)?

### 4. Blast Radius & Scope Containment
- Did the author only touch files within their assigned domain?
- Are there unrelated formatting changes or unnecessary refactoring that bloat the diff?
- Were existing comments and docstrings preserved?

### 5. Documentation & Incident Logging
- If a bug was resolved, is there an entry in `.project_docs/INCIDENT_LOG.md`?
- Were the relevant architecture guides (`DATA_FLOWS.md`, `README.md`) updated?

---

## Review Output Format
The agent must output a structured verdict:
```markdown
### 🔍 Sovereign Code Review Verdict: [APPROVED | CHANGES_REQUESTED]
- **Contracts & Types:** [PASS / FAIL - Details]
- **Test Coverage:** [PASS / FAIL - Details]
- **Security Invariants:** [PASS / FAIL - Details]
- **Blast Radius:** [PASS / FAIL - Details]
- **Documentation:** [PASS / FAIL - Details]

**Summary & Action Items:** [Concise feedback]
```
