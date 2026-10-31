---
name: test-driven-development
description: Enforces strict Test-Driven Development (TDD) using the Red-Green-Refactor loop. Tests must be written and proven to fail before any production implementation code is created. Use when building business logic, creating algorithms, adding API endpoints, or writing automated tests.
---

# Test-Driven Development (TDD) Protocol

> **Objective:** Guarantee 100% test coverage, eliminate regression risks, and prove code correctness using empirical verification before writing production implementations.

---

## When to Use This Skill
- Implementing new core algorithms, cryptographic utilities, or validators.
- Building state machine transition logic or business rules.
- Writing backend API routes, middleware, and database services.
- Adding regression tests during bug resolution.

---

## The Non-Negotiable Red-Green-Refactor Loop

```
[1. RED PHASE] ──► Write an automated test asserting the desired behavior.
        │          Run the test runner $\to$ PROVE IT FAILS.
        ▼
[2. GREEN PHASE] ──► Write the minimal production code needed to pass.
        │            Run the test runner $\to$ PROVE IT PASSES.
        ▼
[3. REFACTOR PHASE] ──► Clean code smells, optimize performance, and document.
                       Re-run the test runner $\to$ PROVE IT STILL PASSES.
```

---

## The 4-Step TDD Workflow

### Step 1: Write the Failing Test (Red)
1. Identify the atomic behavior under test (e.g. `verifyTokenPayload rejects expired tokens`).
2. Construct the test case using the project's test framework (Vitest, Jest, Flutter Test, PyTest).
3. Execute the test runner:
   ```bash
   npm test -- path/to/test.ts # or flutter test test/path_test.dart
   ```
4. **Mandatory Check:** The test **MUST FAIL**. If it passes before you write implementation code, the test is invalid or testing the wrong assertion.

### Step 2: Implement Minimal Code (Green)
1. Write only the code necessary to make the failing test pass.
2. Avoid premature optimization or implementing speculative features.
3. Re-run the test:
   - Verify it now **PASSES**.

### Step 3: Implement Negative & Edge Cases
Do not stop at the "happy path". Write tests asserting:
- Empty or malformed payloads throw structured error codes.
- Out-of-bounds numeric quantities are rejected.
- Tampered cryptographic signatures fail verification.
- Expired timestamps or premature clock skews are rejected.

### Step 4: Refactor with Protection
1. Remove duplication, extract helper functions, and enforce strict type safety.
2. Re-run the entire test suite to guarantee zero collateral regressions.
3. Commit with atomic message: `test(<domain>): implement unit tests and pass suite`.

---

## Anti-Patterns Strictly Forbidden
- ❌ **Testing After the Fact:** Writing all production code and then writing trivial tests to "reach a coverage percentage".
- ❌ **Weak Assertions:** Asserting `expect(result).toBeDefined()` instead of checking the exact payload fields.
- ❌ **Test Masking:** Disabling assertions or deleting tests when code breaks.
