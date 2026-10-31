---
name: diagnosing-bugs
description: Systematic root cause analysis and bug diagnosis protocol using the Five Whys. Prevents superficial masking, error suppression, and unverified patches. Use when an error occurs, tests fail, compiler crashes, or unexpected runtime behavior is observed.
---

# Systematic Bug Diagnosis & Root Cause Analysis Protocol

> **Objective:** Diagnose errors down to their architectural root cause, preventing temporary superficial patches and error masking.

---

## When to Use This Skill
- A runtime error, compiler failure, or HTTP 4xx/5xx status code is encountered.
- An automated test scenario fails unexpectedly.
- A regression is introduced following a refactor or dependency change.
- A user reports broken UI or backend behavior.

---

## The 4-Step Diagnostic Protocol

### Step 1: Capture & Deterministically Reproduce
1. Extract the raw error message, full stack trace, and HTTP status code.
2. Isolate the exact command or network request that triggers the failure.
3. Re-run the command locally to reproduce the failure deterministically. If you cannot reproduce it, gather more telemetry before changing any code.

### Step 2: The Five Whys Root Cause Analysis (RCA)
Trace the error back to its architectural origin:
- *Surface Symptom:* What broke on the surface? (e.g. `TypeError: Cannot read properties of undefined`).
- *Why 1:* Which variable was undefined? (e.g. `authToken`).
- *Why 2:* Why was it not initialized? (e.g. Role switch modal didn't call the login endpoint).
- *Why 3:* Why was the login endpoint omitted? (e.g. Client assumed role switching is purely visual).
- *Why 4 (Root Cause):* Authentication state desynchronization between client role state and server Bearer token middleware.

### Step 3: Anti-Masking Audit (What NOT to Do)
Before writing the fix, verify you are NOT applying any of these banned masking tricks:
- ❌ Do NOT wrap code in an empty `try {} catch (e) {}` that silences the error.
- ❌ Do NOT add `as any` or `@ts-ignore` to silence TypeScript compiler errors.
- ❌ Do NOT insert a hardcoded mock value that bypasses the actual service.
- ❌ Do NOT comment out the failing assertion in the test runner.

### Step 4: Write Failing Regression Test & Fix at Root
1. Write an automated test asserting the expected behavior: verify it **fails** on the current bug.
2. Apply the fix at the root layer (e.g., update the client auth provider to perform the token exchange).
3. Verify the new test passes AND the full project test suite passes with 0 regressions.
4. Record the incident in `.project_docs/INCIDENT_LOG.md`.

---

## The Brutal Truth Diagnostic Format
If a bug cannot be resolved after two attempts, output the **Brutal Truth Diagnostic**:
```markdown
### ⚠️ Factual Blocker Diagnostic
- **Target Component:** `[File path]`
- **Observed Error:** `[Exact error message]`
- **Root Cause Mechanism:** `[Architectural explanation]`
- **Failed Hypotheses:** `[What was attempted and why it failed]`
- **Prerequisites for Resolution:** `[Tokens, permissions, or architectural decision needed]`
```
