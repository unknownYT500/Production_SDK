# ACTION PROTOCOL: REVERTING CHANGES & EMERGENCY ROLLBACK
> **Action Type:** Remedial / Emergency Failsafe Operation  
> **Trigger:** Unrecoverable build failure, cascading test regressions, critical security vulnerability introduced by recent changes, or user request to undo.  
> **Mandatory Invariant:** Clean State Restoration. Zero Orphaned Artifacts. Full Diagnostic Transparency.

---

## 1. The 5-Stage Revert & Rollback Cycle

When a modification causes more instability than the previous working baseline, the AI agent must NOT blindly apply more untested patches. It must execute this 5-stage rollback:

```
[STAGE 1: TRIAGE & REVERT TRIGGER] ──► Identify failure severity; trigger immediate rollback gate.
              │
              ▼
[STAGE 2: GIT WORKING TREE ROLLBACK] ──► Restore codebase to clean pre-change commit/snapshot.
              │
              ▼
[STAGE 3: STATE & DATABASE ROLLBACK] ──► Revert applied database migrations; clear dirty caches.
              │
              ▼
[STAGE 4: CLEANLINESS VERIFICATION] ──► Run compiler & test suite to verify 100% baseline restoration.
              │
              ▼
[STAGE 5: DIAGNOSTIC POST-MORTEM] ──► Publish Factual Blocker Diagnostic explaining failure.
```

---

## 2. Granular Step-by-Step Instructions

### STAGE 1: Triage & Revert Triggers
An emergency revert must be triggered immediately if any of the following occur:
1. **The Three-Strike Rule:** Three consecutive attempts to fix a build error fail and introduce new errors.
2. **Cascading Regression:** A fix for Component A breaks previously passing tests in Component B or C.
3. **Database Corruption Risk:** A migration or script starts corrupting or locking existing production tables.
4. **Security Vulnerability Spike:** A DAST scan or linter detects exposed secrets or open unauthenticated endpoints resulting from recent code.

### STAGE 2: Git Working Tree Rollback
1. Inspect git status:
   ```bash
   git status
   ```
2. If changes are uncommitted:
   - Restore modified tracked files:
     ```bash
     git checkout -- .
     ```
   - Clean untracked scratch files:
     ```bash
     git clean -fd
     ```
3. If changes were committed to a feature branch:
   - Revert the specific commit using `git revert <commit_hash>` to preserve chronological git audit history.

### STAGE 3: Database & State Rollback
1. If a database migration was executed:
   - Identify the down-migration or inverse SQL commands.
   - Execute the inverse SQL script to drop newly created columns/tables and restore prior constraints.
   - Verify that the schema matches the companion mobile/web client expectation.
2. If local caching layers were modified:
   - Purge corrupted IndexedDB, SQLite, or Redis test databases to ensure no orphaned state lingers.

### STAGE 4: Baseline Cleanliness Verification
1. Run the project build command:
   ```bash
   npm run build # or flutter analyze / cargo check
   ```
   - **Must compile with 0 errors.**
2. Run the core system test suite:
   ```bash
   npm run test
   ```
   - **All baseline tests must return green (100% PASS).**

### STAGE 5: Diagnostic Post-Mortem Publication
Log the incident in `.project_docs/INCIDENT_LOG.md` and present the factual diagnostic to the user:
```markdown
### 🔄 Emergency Rollback Executed
- **Rollback Target:** Reverted to commit `[commit_hash]` (Known Good State).
- **Trigger:** Build failure in `web/src/api/security.ts` caused by incompatible dependency imports.
- **Actions Taken:** 
  1. Restored working directory to clean baseline.
  2. Reverted schema migration `20261031_temp.sql`.
  3. Verified system test suite: 20/20 Passing.
- **Root Cause Diagnostic:** The proposed change required `jose@6.x` which conflicted with existing node runtime modules.
- **Next Safe Step:** Isolate the dependency upgrade into a standalone container/subagent before retrying.
```
