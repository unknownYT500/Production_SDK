# Project Post-Mortem: Faults, Roadblocks & Architectural Failsafes

> **Context:** Rigorous technical post-mortem of the **RationSafe / GrainTrust** application lifecycle, analyzing real bugs, edge-case failures, penetration testing findings (ArgosX / Strix), and environment discrepancies encountered during development.  
> **Objective:** Translate every real-world mistake into a hardened, automated failsafe inside the new Sovereign Production SDK.

---

## 1. Executive Fault Analysis Matrix

| # | Subsystem / Area | Observed Failure / Roadblock | Root Cause Mechanism | Battle-Tested Failsafe for the SDK |
|---|---|---|---|---|
| **1** | **Database & RLS** | HTTP 401 on `registrations` upsert during machine heartbeat. | Overloaded table: Storing machine telemetry and citizen PII in the same table. Tightening RLS to protect PII blocked anonymous upserts because PostgreSQL `ON CONFLICT DO UPDATE` requires `SELECT` permissions on conflicting rows. | **Entity Segregation Protocol:** Never overload single tables. Separate public telemetry from private PII at schema design time. Support granular conditional RLS policies. |
| **2** | **Authentication & State** | 401 Unauthorized on KYC verify & approve endpoints. | Client-server auth token disconnect: Role switcher verified password locally/in database, but never completed login handshake with `/api/v1/auth/login` to obtain and attach a valid JWT Bearer token. | **Unified Auth Client Middleware:** An interceptor that automatically exchanges credentials for cryptographic JWTs and transparently injects `Authorization: Bearer <token>` into all outbound requests. |
| **3** | **Runtime Portability** | 500 Internal Server Error / `FUNCTION_INVOCATION_FAILED` on Vercel Edge. | Environment divergence: Calling `res.status().json()` which exists in Express but was missing on native Node.js `http.ServerResponse` during serverless edge invokes. Also, throwing uncaught errors in module top-level scope when env vars were missing. | **Universal Response Abstraction:** Resilient response helpers that safely handle both Express and serverless signatures. Top-level environment guards with deterministic fallbacks. |
| **4** | **Frontend Startup** | Red 401/500 errors in DevTools network tab upon page load. | Unconditional client probing: App invoked `/api/v1/registrations` and `/api/v1/cards` before verifying if running in cloud serverless mode or whether an operator was logged in. | **Auth-Gated Data Fetcher:** Client data layer inspects current authentication context before issuing network requests; unauthenticated states degrade gracefully to clean empty sets or local cache. |
| **5** | **Security & Privacy** | ArgosX DAST audit flagged unauthenticated PII leakage. | Public `SELECT` policies allowed anonymous scraping of citizen phone numbers, dates of birth, and household income. | **Zero-Trust Data Minimization:** Client-side **AES-GCM-256 field-level encryption** before storage; database-level RLS restricting sensitive citizen reads strictly to authenticated roles. |
| **6** | **Cross-Platform CLI** | Python script crashes with `UnicodeEncodeError: 'charmap' codec can't encode characters`. | Windows PowerShell default encoding is CP1252, which fails when scripts output UTF-8 symbols, emojis, or markdown formatting without explicit encoding flags. | **Strict UTF-8 IO Standards:** All SDK automation scripts must explicitly configure `encoding='utf-8'` and avoid unhandled Unicode writes to Windows console streams. |
| **7** | **Repository Isolation** | Risk of accidental edits to companion mobile codebase during web refactoring. | Monorepo shared workspace without mechanical directory barriers. | **Directory Lock & Pre-Commit Guards:** Formal codebase boundaries with automated checks preventing agents or developers from touching protected directories (e.g. `mobile/`). |

---

## 2. Deep-Dive Failure Case Studies

### 2.1 Case Study 1: The Overloaded Table Trap (Supabase 401 on Telemetry)

#### The Problem:
During the hackathon, the client periodically posted machine presence telemetry to Supabase. However, DevTools reported red X `401 Unauthorized` on `/rest/v1/registrations`.

#### The Root Cause:
Early in development, the `registrations` table was used as a generic document store (`id`, `node_id`, `status`, `data: jsonb`). It stored:
1. Citizen KYC intake forms (`id: "01a18b..."`, contains citizen phone numbers, names, income).
2. Machine telemetry pings (`id: "mach_telemetry_..."`).
3. Machine event logs (`id: "mach_log_..."`).
4. Admin config records (`id: "config_admin_credentials"`).

When the independent ArgosX penetration test flagged unauthenticated citizen PII scraping, an RLS policy was applied:
```sql
CREATE POLICY "Authenticated read registrations" ON registrations 
FOR SELECT TO authenticated USING (true);
```
This solved the PII leak. However, the browser client made machine telemetry pings using the public anonymous key:
```typescript
await supabase.from('registrations').upsert({ id: 'mach_telemetry_...', ... });
```
In PostgreSQL, an `UPSERT` translates to `INSERT ... ON CONFLICT DO UPDATE`. When an existing row matches, PostgreSQL **must evaluate the table's `SELECT` policy** on that row before allowing the update. Because `anon` had no `SELECT` policy on `registrations`, PostgreSQL threw error code `42501` (`new row violates row-level security policy for table "registrations"`), and PostgREST returned HTTP 401.

#### The SDK Failsafe:
* **Rule 1 (Schema Purity):** Telemetry, logs, configurations, and PII must live in distinct physical tables. Never use a single table as a catch-all document dump.
* **Rule 2 (Granular RLS by Prefix/Domain):** If polymorphic storage is unavoidable, RLS policies must allow public reads on non-sensitive prefixes:
  ```sql
  CREATE POLICY "Public read non_pii registrations" ON registrations 
  FOR SELECT TO public USING (id LIKE 'mach_%' OR id LIKE 'config_%');
  ```

---

### 2.2 Case Study 2: Client-Server Authentication Desynchronization

#### The Problem:
An operator entered the security password (`'adrenaline'`) in the UI modal. The modal closed and reported success. However, clicking "Verify KYC" or "Approve Card" immediately threw `401 Unauthorized: Access Denied: Missing or malformed cryptographic Bearer token`.

#### The Root Cause:
The UI component only executed:
```typescript
const result = await verifyRolePasswordInSupabase(password, role);
if (result.success) {
  setActiveRole(role);
}
```
The client state changed to `SUPERVISOR`, but **no HTTP Bearer token was ever requested or stored**. The server-side API required `Authorization: Bearer <jwt>`. Because `currentAuthToken` remained an empty string, all subsequent administrative API calls were rejected by server middleware.

Furthermore, on the backend in `server.ts`:
```typescript
account = await authenticateAccount(username, password, role);
```
`authenticateAccount` was undefined due to an incomplete import refactor, throwing a `ReferenceError` caught silently by a try-catch block that returned 401.

#### The SDK Failsafe:
* **Unified Auth Client Module:** The SDK must provide an integrated auth manager:
  ```typescript
  const session = await authClient.login({ username, password, role });
  // Automatically persists token in secure storage, attaches to all fetch clients,
  // and emits reactive session state to UI listeners.
  ```
* **Strict Type Checking on Server Handlers:** Never leave un-imported or mock function references in production route handlers.

---

### 2.3 Case Study 3: The Edge Serverless vs. Local Node Disconnect

#### The Problem:
Endpoints worked flawlessly when tested locally via `npm run start:api` (`localhost:3001`), but failed with `500 FUNCTION_INVOCATION_FAILED` when deployed to Vercel Serverless Edge functions.

#### The Root Cause:
1. **Module Import-Time Failures:** In `auth.ts`, top-level code executed:
   ```typescript
   if (!process.env.JWT_SECRET) throw new Error("JWT_SECRET must be set in production");
   ```
   On Vercel, if an environment variable was missing or named differently, the entire serverless lambda crashed during module import, before the request handler was ever invoked.
2. **Signature Mismatch:** Express attaches convenience methods like `res.status(code).json(data)`. In native Node serverless function adapters, `res` is an instance of `http.ServerResponse`, which does not have `.status()` or `.json()` unless explicitly wrapped.

#### The SDK Failsafe:
* **Graceful Environment Fallbacks:** Core security modules must use hardened fallback secrets in sandbox/serverless environments rather than crashing the process at import time.
* **Universal HTTP Adapter:**
  ```typescript
  function sendJson(res: ServerResponse, status: number, data: unknown) {
    res.setHeader('Content-Type', 'application/json');
    if (typeof (res as any).status === 'function') {
      return (res as any).status(status).json(data);
    }
    res.statusCode = status;
    return res.end(JSON.stringify(data));
  }
  ```

---

### 2.4 Case Study 4: Double-Spending Prevention in Offline Distributed Edge Terminals

#### The Problem:
In rural fair price shops, edge nodes operate without internet connectivity. If two offline nodes disburse grain to the same citizen, total quota depletion can exceed statutory allowances.

#### The Root Cause:
In an offline system, multiple nodes cannot coordinate via a central database mutex or lock.

#### The SDK Failsafe:
* **The Cryptographic Quota Lease Model:** Quotas are never stored as floating counters. Quotas are partitioned into cryptographically signed leases bound to specific edge node IDs with local monotonic counters and Ed25519 vouchers.
* **Deterministic Reconciliation:** When connectivity resumes, batch reconciliation processes outboxes through atomic database stored procedures (`fn_reconcile_sync_batch`) with SHA-256 idempotency deduplication.

---

## 3. Systematic Protocols to Implement in the SDK

1. **Protocol 1: Pre-Flight Integrity Check**
   - Check all required environment variables with explicit type and length assertions.
   - Test database connectivity, schema integrity, and RLS policies prior to accepting production traffic.

2. **Protocol 2: The Controlled Action SOP**
   - Make surgical, minimal code edits. Never rewrite an entire subsystem to fix a localized bug.
   - Verify working trees with `git status` and test suites before and after every modification.
   - Lock down off-scope directories (e.g. `mobile/`).

3. **Protocol 3: Automated Publication-Grade Documentation**
   - Maintain living architecture and API contracts in version-controlled markdown.
   - Provide automated compilation scripts (`generate_tech_book.py`) to convert markdown to print-ready PDF documentation with 1 command.
