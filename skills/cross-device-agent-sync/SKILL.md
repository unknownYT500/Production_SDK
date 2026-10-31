---
name: cross-device-agent-sync
description: Manages cross-device agent concurrency, distributed domain locks, and Git branch isolation. Prevents simultaneous schema collisions, entity corruption, and overwritten code when multiple teammates run AI agents across separate laptops. Use when collaborating in multi-developer or multi-agent teams.
---

# Cross-Device Multi-Agent Synchronization Protocol

> **Objective:** Prevent concurrent AI agents operating on different laptops from corrupting shared database schemas, breaking shared API contracts, or overwriting companion codebases.

---

## When to Use This Skill
- Multiple team members are running autonomous agents on separate computers concurrently.
- One agent is developing the frontend web app while another is developing the mobile terminal or backend API.
- Applying database migrations or altering shared API contracts in a multi-client repository.

---

## The 4 Rules of Multi-Agent Coordination

### Rule 1: Strict Domain Ownership Isolation
Every agent running on a given machine must register its assigned domain:
- **Agent Web:** Write access restricted to `/web/src/client/`.
- **Agent Mobile:** Write access restricted to `/mobile/lib/`.
- **Agent Backend/Database:** Write access restricted to `/web/src/api/` and `/web/supabase/`.
- **Enforcement:** An agent is constitutionally blocked from modifying files in another agent's assigned domain without an explicit cross-domain lease.

### Rule 2: The Database Schema Lock (`LOCK_DOMAIN_DB_SCHEMA`)
Any mutation to shared persistent state (PostgreSQL tables, migrations, RPCs, or shared crypto algorithms) requires acquiring the **Distributed Schema Lock**:
1. Check lock registry (`agent_locks` table or `.agent_locks/SCHEMA.lock`):
   - If FREE $\to$ Acquire lock with a 30-minute lease.
   - If BUSY $\to$ Do NOT apply migrations. Either:
     - Queue the proposed migration in `.pending_migrations/`.
     - Degrade gracefully to local SQLite/IndexedDB mocks for current testing.
2. Apply migration cleanly.
3. Commit and push migration to repository.
4. Release lock immediately upon completion.

### Rule 3: Git Feature Branch Isolation
- Agents on separate machines **must never push directly to `main`**.
- Work must be committed to dedicated feature branches:
  - `agent/<device_name>/<feature>`
- Changes are merged into `main` exclusively via Pull Requests reviewed by the primary orchestrating agent or human lead.

### Rule 4: Graceful Offline Degradation
If an agent cannot contact the central database or the lock is held:
- The agent must never stall or throw unhandled exceptions.
- It must seamlessly route operations to local SQLite, IndexedDB, or mock storage engines until central locks become available.
