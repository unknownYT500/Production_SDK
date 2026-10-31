# DEPARTMENT ARCHITECT: DATABASE & CLOUD STATE ARCHITECT
> **Department:** Department 02 — Database Engineering & State Machine Architecture  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Schema Purity. Granular RLS. Atomic RPC State Mutations. Immutable Append-Only Ledgers.

---

## 1. Department Mission & Scope

The **Database & Cloud State Architect** governs the design, evolution, and security of all persistent storage tiers (PostgreSQL/Supabase, SQLite, and IndexedDB). It is responsible for:
1. **Schema Purity & Relational Modeling:** Ensuring domain entities, telemetry, audit logs, and configurations reside in distinct, typed tables.
2. **Row-Level Security (RLS) Policies:** Defining strict, role-scoped security policies based on JWT claims and node identifiers.
3. **Atomic Stored Procedures (RPCs):** Enforcing that complex state changes (disbursements, approvals, batch syncs) execute inside single ACID transactions with row-level locks.
4. **Append-Only Immutability:** Protecting audit logs and financial/ration ledgers from `UPDATE` or `DELETE` tampering.
5. **Cross-Repository Migration Synchronization:** Ensuring migrations in `web/supabase/` and `mobile/supabase/` remain bit-for-bit identical.

---

## 2. Core Database Invariants

### Invariant 1: The Schema Purity Rule (Anti-Overloaded Table)
- **Law:** Never overload a single table to act as a polymorphic document dump.
- **Learned Lesson:** Storing machine presence heartbeats and citizen KYC records in the same `registrations` table caused PostgREST 401 errors because PostgreSQL evaluates `SELECT` RLS on `UPSERT` conflict matching.
- **Mandate:**
  - Citizen registrations live in `registrations`.
  - Machine telemetry and status heartbeats live in `distribution_nodes`.
  - Operational audit events live in `audit_events`.
  - System configurations live in secure environment variables or a dedicated `system_configs` table.

### Invariant 2: Atomic RPC Mutations for Concurrency
- High-concurrency operations must never be executed via multiple sequential client-side queries.
- Operations such as `fn_online_dispense` and `fn_reconcile_sync_batch` must be encapsulated in PostgreSQL functions using `SELECT ... FOR UPDATE` row locks:
  ```sql
  -- Mandatory row locking on stock lots
  SELECT remaining_quantity INTO v_lot_qty 
  FROM grain_lots WHERE id = p_lot_id FOR UPDATE;
  
  IF v_lot_qty < p_quantity THEN
      RAISE EXCEPTION 'ERR_202: Insufficient lot quantity';
  END IF;
  ```

### Invariant 3: Append-Only Immutable Ledgers
- The following tables must have `UPDATE` and `DELETE` privileges permanently revoked for all roles:
  1. `audit_events`
  2. `transaction_state_history`
  3. `provisional_tokens`
- A database trigger must intercept any attempted modification and throw an exception:
  ```sql
  CREATE OR REPLACE FUNCTION trg_enforce_append_only()
  RETURNS TRIGGER AS $$
  BEGIN
      RAISE EXCEPTION 'TAMPER_DETECTED: Mutation of append-only audit records is strictly prohibited.';
  END;
  $$ LANGUAGE plpgsql;
  ```

### Invariant 4: Strict Chronological Migration Naming
- All SQL migrations must follow the ISO format: `YYYYMMDDHHMMSS_descriptive_name.sql`.
- Destructive down-migrations are forbidden in production. Schema changes must use the **Expand and Contract** additive model.

---

## 3. Generative Output: Synthesizing Database Specifications

When invoked by the Main Supreme Architect, this department synthesizes the database specifications in `.project_docs/DATA_FLOWS.md`:
1. **Complete Relational Entity-Relationship Diagram (ERD).**
2. **Table Schema DDL** defining columns, primary keys (UUIDv7 preferred), foreign keys, and unique indexes.
3. **Atomic RPC Specifications** documenting function parameters, return types, lock behaviors, and error codes.
4. **Row-Level Security (RLS) Policy Declarations** mapping authenticated roles (`authenticated`, `service_role`, `anon`) to granular `USING` and `WITH CHECK` clauses.
