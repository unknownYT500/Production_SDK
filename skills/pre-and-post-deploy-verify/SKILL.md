---
name: pre-and-post-deploy-verify
description: Enforces rigorous pre-deployment build verification and post-deployment live health checks. Catches cold-start 500 crashes, missing environment variables, SSL handshake errors, and broken routes. Use before and immediately after deploying to staging or production.
---

# Pre- and Post-Deployment Verification Protocol

> **Objective:** Ensure applications deploy smoothly to production environments without crashing on startup, leaking secrets, or failing health probes.

---

## When to Use This Skill
- Prior to pushing commits that trigger production CI/CD builds (e.g. Vercel, Netlify, Cloud Run).
- Immediately after a production deployment goes live.
- When diagnosing post-deployment HTTP 500 errors or environment variable failures.

---

## Phase 1: Pre-Deployment Verification Gate

Before running any deployment command or pushing to the production branch:

### 1. Static Typecheck & Bundling Audit
Execute production compile command locally:
```bash
npm run build # or flutter build apk / cargo build --release
```
- **Must compile with zero errors.**
- Inspect the generated bundle size: Main bundle should not exceed target budgets.

### 2. Environment Variable Audit
Verify that all required production environment variables are configured in the cloud host:
- `JWT_ISSUER`, `JWT_AUDIENCE`, `JWT_SECRET` (or `JWT_JWKS_URL`).
- `ALLOWED_ORIGINS` (must be explicit bare HTTPS origins, no `localhost`).
- Database connection strings and Supabase public keys.
- **Top-Level Guard Check:** Verify that no module throws synchronous unhandled exceptions during module load if optional environment variables are missing.

### 3. Comprehensive Test Suite Execution
Execute the full system test runner:
```bash
npm test
```
- Assert that **100% of test scenarios pass** before deploying.

---

## Phase 2: Post-Deployment Verification Gate

Immediately after the deployment is completed:

### 1. Live Root & Health Endpoint Probes
Execute curl requests against the live URL:
```bash
curl -I https://your-production-app.com/api/v1/health
```
- Verify status code: **HTTP 200 OK**.
- Verify latency: Response time $< 500$ ms.

### 2. HTTP Edge Security Header Verification
Inspect headers on the live response:
```bash
curl -sI https://your-production-app.com
```
- Assert presence of:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Strict-Transport-Security: max-age=...`

### 3. Clean Browser Startup Inspection (Zero Console Errors)
Inspect the Network waterfall of a cold-boot browser session:
- **Zero Red HTTP Status Codes:** No unauthenticated 401/404/500 errors on initial page load.
- If endpoints require authentication, verify that the client suppresses network calls until the user logs in.
- Verify WebSocket / Realtime CDC connection stabilizes and receives heartbeat messages.
