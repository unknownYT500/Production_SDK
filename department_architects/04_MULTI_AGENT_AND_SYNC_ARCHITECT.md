# DEPARTMENT ARCHITECT: MULTI-AGENT & TEAM SYNC ARCHITECT
> **Department:** Department 04 — Distributed Agent Coordination & Multi-Device Synchronization  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Distributed Domain Locks. Isolated Git Feature Branches. Agent-to-Agent PR Review. Zero Concurrent Schema Mutations.

---

## 1. Department Mission & The Multi-Device Dilemma

In collaborative team settings (such as hackathons or multi-developer projects), different team members run autonomous coding agents (like Antigravity) on separate laptops:
- **Developer 1's Agent** is building the Web Dashboard.
- **Developer 2's Agent** is building the Mobile Android Terminal.
- **The Disaster Scenario Encountered:** Both agents simultaneously execute migrations against the same cloud database (Supabase), add conflicting columns, delete each other's test records, and push conflicting Git commits, resulting in `null` entities and corrupted application states.

This department establishes a **Distributed Concurrency Protocol** ensuring that multi-agent teams work in harmony without clobbering schemas or overwriting code.

---

## 2. Core Synchronization Invariants

### Invariant 1: Domain Ownership Isolation
Every agent running in a project workspace is assigned an exclusive **Domain Ownership Boundary**:
- **Agent Alpha (Web):** Has write permissions to `/web/`. Read-only access to `/mobile/`.
- **Agent Beta (Mobile):** Has write permissions to `/mobile/`. Read-only access to `/web/`.
- **Agent Gamma (Backend/DB):** Has write permissions to `/web/src/api/` and `/web/supabase/`.
- **Violation Guard:** If Agent Alpha attempts to modify a file inside `mobile/`, the agent must immediately abort and request an explicit domain transfer lease.

### Invariant 2: The Distributed Domain Lock (`agent_locks`)
Any operation that mutates shared central state (e.g., executing a Supabase migration, updating central API route signatures, changing shared crypto algorithms) requires acquiring a **Distributed Domain Lock**.

#### Lock Storage Mechanisms:
1. **Cloud Database Lease (Supabase `agent_locks` table):**
   ```sql
   CREATE TABLE IF NOT EXISTS agent_locks (
       domain TEXT PRIMARY KEY,          -- e.g. 'DB_SCHEMA', 'CENTRAL_API'
       acquired_by TEXT NOT NULL,        -- e.g. 'agent_alpha_macbook'
       lease_expires_at TIMESTAMPTZ NOT NULL,
       metadata JSONB
   );
   ```
2. **Git-Based Lockfile Fallback (`.agent_locks/`):**
   When operating offline or without database access, agents acquire locks by creating an atomic lockfile (`.agent_locks/SCHEMA.lock`) committed to a shared synchronization branch.

#### Lock Acquisition Rules:
- If `DB_SCHEMA` lock is held by Agent Alpha, Agent Beta **MUST NOT execute migrations**.
- Agent Beta must either:
  1. Queue the desired schema change in a pending queue file (`.pending_schema_requests.json`).
  2. Degrade gracefully to local SQLite/mock testing until the lock expires or is released.

### Invariant 3: Git Branch & Pull Request Review Pipeline
- Agents on separate machines **must never push directly to `main`**.
- All agent work must be committed to dedicated feature branches:
  - `agent/web-lead-<task>`
  - `agent/mobile-lead-<task>`
- **The Agent-to-Agent PR Review Protocol:**
  - Before merging into `main`, the primary orchestrating agent acts as the **CI Reviewer Agent**.
  - The reviewer agent runs:
    1. Static linter and compilation checks across both repositories.
    2. The full 20-scenario system test suite.
    3. Git diff analysis to confirm the PR touches only its assigned domain folder.
  - If all checks pass, the PR is merged into `main`, triggering automated deployment on Vercel.

---

## 3. Generative Output: Synthesizing Multi-Agent Config

When invoked, this department generates:
1. `.agent_domain_config.json` defining active workspace path boundaries for the current device.
2. Cross-agent communication scripts (`agent_lock.py` or `.agent_locks/`).
3. PR review guidelines in `.project_docs/ROADMAP.md`.
