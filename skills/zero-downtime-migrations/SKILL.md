---
name: zero-downtime-migrations
description: Enforces the Expand and Contract pattern, schema purity, and atomic stored procedures for safe, zero-downtime database migrations. Prevents table overloading, breaking column renames, and RLS conflicts. Use when adding tables, changing columns, writing migrations, or syncing schemas across clients.
---

# Zero-Downtime Database Migration Protocol

> **Objective:** Evolve database schemas safely without causing downtime, breaking companion clients, or triggering RLS permission conflicts.

---

## When to Use This Skill
- Creating new database tables, indexes, or relationships.
- Adding, renaming, or modifying existing columns.
- Writing atomic PostgreSQL stored procedures (RPCs).
- Synchronizing database schemas between companion web and mobile codebases.

---

## Core Invariant 1: The Schema Purity Rule
- **Never overload a single table** to store both public telemetry/logs and private user records.
- Storing unauthenticated machine heartbeats and citizen KYC records in the same table breaks PostgREST `UPSERT` operations because PostgreSQL evaluates `SELECT` RLS policies during conflict checks.
- Keep domain entities, telemetry, logs, and system configs in distinct, typed tables.

---

## Core Invariant 2: The Expand and Contract Pattern
Never rename or delete an active database column in a single step. Follow the 4-phase rollout:

```
[PHASE 1: EXPAND] ──► Add new column/table as NULLABLE.
          │           Existing apps continue writing to old column.
          ▼
[PHASE 2: DUAL-WRITE] ──► Update application code to write to BOTH old and new columns.
          │               Backfill historical data asynchronously.
          ▼
[PHASE 3: READ-SWITCH] ──► Switch all client/API queries to read from the NEW column.
          │                Verify zero errors across all connected clients.
          ▼
[PHASE 4: CONTRACT] ──► In a subsequent release, remove old column and cleanup triggers.
```

---

## Core Invariant 3: Atomic RPCs with Explicit Row Locks
High-concurrency mutations (balances, inventory claims, quota allocations) must be encapsulated inside atomic PostgreSQL stored procedures:
```sql
CREATE OR REPLACE FUNCTION fn_atomic_mutation(p_id TEXT, p_qty REAL)
RETURNS JSONB AS $$
DECLARE
    v_balance REAL;
BEGIN
    -- 1. Explicit Row Lock
    SELECT balance INTO v_balance FROM accounts WHERE id = p_id FOR UPDATE;
    
    -- 2. Guard Check
    IF v_balance < p_qty THEN
        RAISE EXCEPTION 'ERR_INSUFFICIENT_BALANCE';
    END IF;
    
    -- 3. Atomic Mutation
    UPDATE accounts SET balance = balance - p_qty WHERE id = p_id;
    
    RETURN jsonb_build_object('status', 'SUCCESS', 'new_balance', v_balance - p_qty);
END;
$$ LANGUAGE plpgsql;
```

---

## Checklist Before Applying Any Migration
1. Migration file is named with chronological ISO timestamp: `YYYYMMDDHHMMSS_description.sql`.
2. Row-Level Security is enabled on every new table.
3. RLS policies are explicitly defined for `authenticated`, `service_role`, and `anon`.
4. Migration is tested against staging before being applied to production.
5. Migration file is copied to companion client folders (e.g. `mobile/supabase/migrations/`) to maintain cross-repo parity.
