# ACTION PROTOCOL: ADDITION OF NEW FEATURE
> **Action Type:** Constructive Engineering Operation  
> **Trigger:** New functional requirement, user story, hackathon milestone, or capability expansion.  
> **Mandatory Invariant:** Interface-First, Spec-Compliant, Zero Architectural Drift, 100% Test-Covered.

---

## 1. The 6-Stage Feature Addition Cycle

Every new feature added by an AI agent must progress through these six gated stages:

```
[STAGE 1: SPECIFICATION & COMPLIANCE] ──► Validate alignment with project spec, rules & rubrics.
              │
              ▼
[STAGE 2: INTERFACE & CONTRACT DESIGN] ──► Define TypeScript/Dart types, schemas & API contracts.
              │
              ▼
[STAGE 3: CONTEXT & COMPLEXITY BUDGET] ──► Decompose into atomic subtasks; assess context limits.
              │
              ▼
[STAGE 4: ATOMIC IMPLEMENTATION] ──► Implement core logic $\to$ storage $\to$ UI in strict order.
              │
              ▼
[STAGE 5: VERIFICATION & AUDIT] ──► Write unit, integration & negative tests; verify build.
              │
              ▼
[STAGE 6: LIVING DOCS & ARCHITECTURE] ──► Update DATA_FLOWS.md, README, and API schemas.
```

---

## 2. Granular Step-by-Step Instructions

### STAGE 1: Specification & Regulatory Review
1. Confirm the feature aligns with the core product mission and hackathon rubrics.
2. Check for regulatory compliance (e.g. DPDPA 2023, NFSA 2013, GDPR):
   - Does this feature introduce citizen Personally Identifiable Information (PII)?
   - If yes, client-side AES-GCM-256 field encryption is mandatory.
3. Verify that the feature does not duplicate existing capabilities or introduce redundant libraries.

### STAGE 2: Interface-First Contract Design
1. **Never write implementation code first.**
2. Define pure TypeScript types, Dart models, or Zod schemas in the domain types file:
   - Request and response payloads.
   - Database table schema and foreign key relationships.
   - Error reason codes (e.g. `ERR_401`, `ERR_403`, `ERR_500`).
3. Ensure the interface uses canonical data representations:
   - Deterministic UUIDv7 IDs.
   - ISO-8601 UTC timestamps.
   - Normalized numeric values (avoid floating-point representation ambiguities).

### STAGE 3: Context & Complexity Budgeting
1. Estimate the scale of the implementation:
   - If $>250$ lines of code or $>3$ files are touched, split the implementation into discrete **Waves**:
     - **Wave 1:** Core types, database migrations, and RPCs.
     - **Wave 2:** Backend API routes, services, and security middleware.
     - **Wave 3:** Frontend UI components, state providers, and local storage fallback.
     - **Wave 4:** End-to-end integration tests and documentation.
2. Ensure working memory is clean before starting each wave.

### STAGE 4: Atomic Implementation Progression
1. **Data Layer First:** Create database migration file (e.g. `supabase/migrations/YYYYMMDD_feature.sql`) and apply Row-Level Security policies.
2. **Business Engine Second:** Implement deterministic logic in pure modules (free of UI dependencies).
3. **API / Transport Third:** Expose route with Zod input validation, rate limiting, and RBAC middleware.
4. **UI Layer Last:** Build ergonomic, accessible UI components adhering to GovTech/enterprise design standards (avoiding AI slop).

### STAGE 5: Comprehensive Verification
1. **Positive Path:** Verify successful execution under standard conditions.
2. **Negative Paths:** Assert proper error throwing under:
   - Invalid field format (`ERR_101`).
   - Expired or malformed cryptographic tokens (`ERR_301`, `ERR_402`).
   - Unauthorized role or missing JWT token (`401 Unauthorized`).
   - Rate limit exhaustion (`429 Too Many Requests`).
3. Run project build command (`npm run build` / `flutter build`) $\to$ Must compile with 0 errors.

### STAGE 6: Living Documentation Update
1. Update `DATA_FLOWS.md` with new boundary interactions and packet flows.
2. Document new API endpoints in `README.md` or OpenAPI spec.
3. Commit with atomic message: `feat(<domain>): implement <feature_name> with full test suite`.
