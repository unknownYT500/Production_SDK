---
name: security-audit
description: Audits codebases for security vulnerabilities, secret leaks, OWASP Top 10 risks, insecure dependencies, and data privacy compliance. Use before submitting code, prior to release, or during penetration testing and security reviews.
---

# Security Audit & Vulnerability Scanning Protocol

> **Objective:** Detect and remediate security vulnerabilities, secret leaks, and unauthenticated data exposures before code is deployed to staging or production.

---

## When to Use This Skill
- Before merging pull requests or committing sensitive changes.
- Prior to deploying to staging or production environments.
- After implementing authentication, authorization, or database access layers.
- When conducting DAST / SAST vulnerability audits.

---

## The 4-Stage Security Audit Checklist

### Stage 1: Secret Leakage & Credential Scan
Scan the working directory and git history for accidentally committed credentials:
- Run regex searches for known secret formats:
  - Private Keys: `BEGIN PRIVATE KEY`, `ed25519_secret`
  - Cloud / Database Tokens: `SUPABASE_SERVICE_ROLE_KEY`, `sk_live_`, `AIzaSy`
  - Hardcoded Passwords: `password\s*=\s*['"][^'"]+['"]`
- **Failsafe:** Verify that `.env` is listed in `.gitignore` and `.env.example` contains only placeholder values (`your_key_here`).

### Stage 2: Data Privacy & PII Protection Audit
1. Inspect all database schemas and network payloads for citizen/customer PII:
   - Are phone numbers, dates of birth, incomes, or government IDs sent in plaintext?
2. Enforce client-side **AES-GCM-256 field encryption** or SHA-256 identifier hashing before data is stored or transmitted.
3. Ensure no PII appears in client-side URLs (query parameters) or plaintext logging streams.

### Stage 3: OWASP Top 10 & API Access Control Audit
1. **Broken Object-Level Authorization (BOLA / IDOR):**
   - Verify that requests for `/resource/:id` validate that the authenticated user owns or has explicit permission to access that resource.
2. **Row-Level Security (RLS) Inspection:**
   - Verify that every PostgreSQL table has RLS enabled (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY;`).
   - Confirm there are **no wide-open policies** (`USING (true)` or `WITH CHECK (true)`) on tables storing sensitive data.
3. **Negative Probe Verification:**
   - Execute an unauthenticated probe using only the public `anon` key $\to$ Assert **0 records returned**.

### Stage 4: Production Edge Security Headers
Inspect reverse proxy or serverless configuration (`vercel.json`, Nginx):
- `X-Content-Type-Options: nosniff` (Blocks MIME-sniffing attacks).
- `X-Frame-Options: DENY` (Blocks Clickjacking).
- `X-XSS-Protection: 1; mode=block` (Blocks browser-level XSS).
- `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload` (Enforces HTTPS).
- `Content-Security-Policy: ...` (Restricts script and connect origins).
