# Sovereign Production Engineering SDK (SovereignSDK)

> **Origin:** Born from real-world engineering trials, high-stress architectural sprints, and rigorous independent penetration testing of the **RationSafe / GrainTrust** mission-critical public distribution platform.  
> **Mission:** To transform hard-earned hackathon learnings, operational failsafes, and discipline into a reusable, production-grade Software Development Kit (SDK) and architectural framework. Next time we build an enterprise or GovTech application, every decision will follow a calculated, controlled, and battle-tested protocol.

---

## 🏛️ Why This SDK Exists

Building mission-critical systems under tight deadlines exposes the subtle cracks that exist in standard web and cloud practices:
* **The "Happy Path" Fallacy:** Systems often work when online, but collapse into cascading 401s, 500s, or uncaught exceptions during network degradation or offline edge operations.
* **Security vs. Usability Friction:** Hardening a database with Row-Level Security (RLS) can accidentally break legitimate background telemetry or unauthenticated public kiosk functions if data boundaries are not architected cleanly from Day 1.
* **Ad-Hoc Architecture Drift:** Without formal state machines and strict data contracts, state variables drift, leading to race conditions, double-spending vulnerabilities, and untraceable bugs.
* **Documentation as an Afterthought:** Trying to write technical specifications, compliance reports, and defense guides at the end of a project is chaotic. Documentation and publication-grade reporting must be built directly into the engineering loop.

---

## 📦 Directory Structure

```
SDK/
├── README.md                      # This manifesto and SDK architectural blueprint
├── raw_notes.md                   # Staging area for raw developer notes, hurdles & observations
└── SDK_development/               # Core analytical laboratory and engineering incubator
    ├── README.md                  # Development methodology, milestones & checklists
    ├── faults_and_failsafes_analysis.md # Comprehensive post-mortem of project hurdles & fixes
    ├── protocols/                 # Standard Operating Procedures (SOPs) for development
    ├── modules/                   # Core SDK libraries (Logging, Auth, DB, Crypto, Outbox)
    └── templates/                 # Reusable production templates (Express, React, Supabase)
```

---

## 🛡️ The 6 Core SDK Pillars

```
+---------------------------------------------------------------------------------------------------+
|                                     SOVEREIGN SDK PILLARS                                         |
+---------------------------------------------------------------------------------------------------+
|  1. Structured Observability   : Structured JSON, W3C Distributed Tracing, Zero-PII Log Guard    |
|  2. Hardened Data Access Layer : Multi-tier fallback, atomic RPCs, strict RLS separation          |
|  3. Cryptographic Invariants   : Canonical RFC 8785 JSON, Ed25519 signing, AES-GCM-256 vault       |
|  4. Deterministic State Logic  : Formal finite-state machines, idempotent deduplication           |
|  5. Living Documentation Habit : Markdown-driven specifications, automated PDF report generation  |
|  6. Safe Release Engineering   : Surgical git commits, directory protection, automated pentesting |
+---------------------------------------------------------------------------------------------------+
```

### 1. Structured Observability & Telemetry
- Never use raw `console.log` in production.
- Structured JSON logs with standard metadata: timestamp, log level, request ID, trace context, and error category.
- PII-sanitization filters that automatically scrub phone numbers, Aadhaar IDs, and private tokens before strings touch standard output.

### 2. Zero-Leakage Data Access Layer (DAL)
- Strict separation between **Public Operational Data** (machine telemetry, depot status, granary stocks) and **Sensitive Citizen Data** (KYC records, income, demographics).
- Never overload a single database table to store both sensitive records and unauthenticated telemetry.
- All high-concurrency mutations must execute via atomic database stored procedures (RPCs) with explicit row locking.

### 3. Cryptographic Invariants & Fault-Tolerant Edge Computing
- Pure TypeScript asymmetric cryptography (Ed25519) running identically in browser WebWorkers, Node.js, and mobile environments.
- Deterministic canonicalization (RFC 8785) preventing key-order signature validation failures.
- Offline-first durable outbox queue with exponential backoff and SHA-256 idempotency deduplication.

### 4. Deterministic Finite-State Machines
- Core business workflows (payments, grain disbursals, order fulfillment) must be modeled as strict mathematical state machines.
- State transitions must be validated against a formal transition matrix, rejecting illegal jumps or state rollbacks with structured error codes.

### 5. Automated Publication-Grade Reporting Habit
- Architectural diagrams, API specifications, and security audits maintained continuously in version-controlled Markdown.
- One-click headless conversion pipelines to generate publication-grade PDF manuals with typography, syntax highlighting, and visual callouts.

### 6. Controlled Release Engineering & Git Protocols
- "Stop-and-Verify" discipline before making destructive changes.
- Surgical, minimal diffs with zero unrelated refactoring.
- Directory locks ensuring critical client folders (e.g., `mobile/`) remain 100% untouched while backend or web systems are modified.
- Automated regression test suites and independent DAST pentest scripts executing before any production deployment.
