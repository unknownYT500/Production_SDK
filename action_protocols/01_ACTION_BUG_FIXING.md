# ACTION PROTOCOL: BUG FIXING & ERROR RESOLUTION
> **Action Type:** Corrective Engineering Operation  
> **Trigger:** Runtime exception, failing test scenario, network 4xx/5xx error, DAST vulnerability, or unexpected state behavior.  
> **Mandatory Invariant:** Zero Band-Aid Fixes. Never mask an error. Always write a regression test.

---

## 1. The 6-Stage Bug Resolution Cycle

Every bug fix undertaken by an AI agent must strictly follow this sequential 6-stage lifecycle:

```
[STAGE 1: REPRODUCE & ISOLATE] ──► Reproduce failure deterministically with minimal command/curl.
              │
              ▼
[STAGE 2: ROOT CAUSE ANALYSIS] ──► Trace error to architectural origin (never treat surface symptom).
              │
              ▼
[STAGE 3: FAILING REGRESSION TEST] ──► Write automated test that fails on the bug and passes on fix.
              │
              ▼
[STAGE 4: ARCHITECTURAL REPAIR] ──► Modify source code at root layer. Zero hacks or mocks.
              │
              ▼
[STAGE 5: FULL SUITE VERIFICATION] ──► Run 100% of test suite. Verify zero collateral regressions.
              │
              ▼
[STAGE 6: AUDIT & INCIDENT LOG] ──► Record in INCIDENT_LOG.md with Prompt ID, Root Cause & Failsafe.
```

---

## 2. Granular Step-by-Step Instructions

### STAGE 1: Deterministic Reproduction
1. Extract the exact error message, stack trace, and HTTP status code.
2. Identify the triggering input, payload, or network condition.
3. Re-run the failing flow via automated command, script, or `curl`:
   - *Example:* `npx tsx src/tests/system.test.ts` or `curl -I https://app.example.com/api/v1/cards`
4. If the bug cannot be reproduced deterministically, stop and gather more telemetry. Do NOT guess.

### STAGE 2: Deep Root Cause Analysis (RCA)
Ask the **Five Whys** to locate the architectural origin:
- *Surface Symptom:* Supabase returns HTTP 401 on `registrations` upsert.
- *Why 1:* PostgREST threw error `42501: new row violates row-level security policy`.
- *Why 2:* The table's RLS policy requires authenticated roles for `SELECT`.
- *Why 3:* `UPSERT` translates to `INSERT ... ON CONFLICT DO UPDATE`, requiring a `SELECT` check on matching rows.
- *Why 4:* The browser client used the public `anon` key to ping machine telemetry.
- *Why 5 (Root Cause):* **Overloaded Table Antipattern.** Telemetry pings and citizen PII were dumped into the same table instead of being properly segregated.

### STAGE 3: The Failing Regression Test Invariant
Before modifying a single line of production code, write an automated test that asserts the correct behavior:
- Run the test: It **MUST FAIL** on the current codebase.
- This proves the test accurately captures the bug and prevents future regressions.

### STAGE 4: Root-Level Architectural Repair
1. **Apply the fix at the root source:**
   - If the schema is overloaded, create a migration to segregate the tables.
   - If a JWT is missing, update the client auth interceptor to perform the login handshake.
   - If serialization order causes hash mismatch, enforce canonical RFC 8785 sorting.
2. **Strictly Forbidden Antipatterns:**
   - ❌ Commenting out failing assertions.
   - ❌ Wrapping code in empty `try {} catch (e) {}` blocks.
   - ❌ Hardcoding bypass flags (e.g. `if (isDev) return true;` in production auth checks).
   - ❌ Changing function signatures without updating all caller locations.

### STAGE 5: Non-Regression Verification
1. Run the new regression test $\to$ Verify it now **PASSES**.
2. Run the **entire existing project test suite** $\to$ Verify **100% PASS** rate.
3. Capture the terminal output as proof.

### STAGE 6: Incident Documentation & Prompt Labeling
Append a structured incident entry into `.project_docs/INCIDENT_LOG.md`:
```markdown
## Incident Log: INC-[YYYYMMDD]-[INDEX]
- **Timestamp:** 2026-10-31T15:45:00+05:30
- **Triggering Prompt:** PROMPT-[LABEL] (e.g. "Fix 401 error on registration submit")
- **Component Affected:** `web/src/client/secure-storage-db.ts` & `supabase/migrations/`
- **Symptom:** HTTP 401 Unauthorized during machine telemetry heartbeat.
- **Root Cause:** Overloaded table with conflicting RLS policies between anon telemetry and authenticated citizen PII.
- **Applied Fix:** Segregated machine heartbeats into dedicated `distribution_nodes` table; updated client sync caller.
- **Verification Proof:** `npx tsx src/tests/system.test.ts` (20/20 Passing).
- **Permanent Failsafe Added:** Schema purity rule added to Database Architect protocol.
```
