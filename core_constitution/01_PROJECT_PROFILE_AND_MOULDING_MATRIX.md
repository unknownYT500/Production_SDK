# PROJECT PROFILE & DYNAMIC MOULDING MATRIX
> **Status:** Constitutional Adaptation Framework  
> **Purpose:** Defines how the Sovereign AI Governance SDK dynamically adapts and moulds its protocols, strictness, security layers, storage tiers, and verification gates according to the specific technical archetype of the target project.

---

## 1. The Dynamic Moulding Philosophy

One size does NOT fit all:
- An offline rural mobile terminal requires extreme battery conservation, local SQLite caching, and asymmetric cryptographic signing.
- A cloud SaaS dashboard requires strict CORS, asymmetric JWT validation, distributed Redis rate limiting, and WebSocket Change Data Capture.
- A quick internal CLI tool requires cross-platform terminal compatibility and zero-dependency packaging.

The **Sovereign SDK** uses a **Profile Matrix**: when an AI begins or reverse-engineers a project, it first evaluates the project against this matrix. The active profile then unlocks specific constitutional mandates and mutes irrelevant requirements.

```
                                  +---------------------------------------+
                                  |        INPUT: PROJECT DISCOVERY       |
                                  | (Source Code, Prompts, Rulebooks, PRD)|
                                  +-------------------+-------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |       PROJECT PROFILE EVALUATION      |
                                  +-------------------+-------------------+
                                                      |
         +--------------------+-----------------------+-----------------------+--------------------+
         |                    |                       |                       |                    |
         v                    v                       v                       v                    v
  [PROFILE: WEB]      [PROFILE: MOBILE]       [PROFILE: DUAL]         [PROFILE: API]       [PROFILE: AI/ML]
  - React/Vite/Next   - Flutter/Dart/Swift    - Sovereign Web + Edge   - Node/Go/FastAPI    - Small Edge Models
  - Strict CSP/CORS   - SQLite/Android Key    - Offline FSM & Sync    - Redis Limiter/JWT  - Quantized INT4
  - Responsive Theme  - Ephemeral QR / Low-RAM- Canonical JSON RFC    - Database RLS/RPC   - 242 Dialect Engine
```

---

## 2. Archetype Specification Matrix

| Dimensional Attribute | Profile 1: Web Application | Profile 2: Mobile Edge Terminal | Profile 3: Sovereign Dual-Architecture | Profile 4: Backend / Microservice | Profile 5: AI / Machine Learning |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Typical Stack** | React 19, Vite, Next.js, TypeScript, Tailwind/CSS | Flutter 3, Dart, React Native, Swift, Kotlin | React 19 + Flutter 3 + PostgreSQL (Supabase) + Express | Node Express 5, Go, FastAPI, PostgreSQL, Redis | PyTorch, ONNX, GGUF, Python, Adaption Labs AI |
| **Network Assumption** | High / Intermittent Web Connectivity | Zero / Unreliable / Low-Bandwidth | Completely Asynchronous (Offline-First $\to$ Sync) | High Availability / Cloud Multi-AZ | Cloud Training $\to$ Quantized On-Device Edge |
| **Primary Storage Layer** | Encrypted IndexedDB (Dexie) + LocalStorage | Local SQLite (`sqflite`) + Secure Keystore | Multi-Tier: SQLite + IndexedDB + PostgreSQL Cloud | Authoritative PostgreSQL + Redis Cache | In-Memory Tensors + Vector Index + Local Files |
| **Security Grounding** | DPDPA 2023, CSP Nonces, Strict Bare CORS | Android Keystore Hardware Isolation, Ed25519 | Zero-Trust Asymmetric Signing + Row-Level Security | Asymmetric JWKS, Rate Limiters, Sanitization | Data Privacy Vault, Masked Fine-Tuning Corpora |
| **Verification Gate** | Headless Build, DevTools Network Audit, Vitest | Dart Static Analysis, Emulator UI Test, Unit | End-to-End Cross-Platform Serialization & ACK Sync | Load Testing, Integration Test Suite, RLS Audit | Benchmark Win-Rate, Latency Benchmarks (<50ms) |
| **Design Priority** | GovTech/Editorial Theme, Responsive Desktop/Pad | Ergonomic Large Touch Targets, High Sunlight Contrast | Visual Brand Parity across Mobile & Web Dashboards | Strict OpenAPI 3.1 Specs, Clean JSON Error Codes | Explainable Inference Logs, Latency Telemetry |

---

## 3. Dynamic Protocol Moulding Rules

When an action is initiated, the Master Architect loads the specific profile and adjusts operational protocols:

### Rule 1: Network Failure Strategy Moulding
- **IF Profile contains `MOBILE` or `SOVEREIGN_DUAL`:**
  - Network disconnection is treated as a **normal operational state**, NOT an exception.
  - The agent is forbidden from displaying blocking error popups or failing requests when offline.
  - Must automatically route mutations to a persistent **Durable Outbox Queue** (`outbox_tokens`) with monotonic state tracking.
- **IF Profile is `WEB_ONLY`:**
  - Offline mode must degrade gracefully to read-only cached IndexedDB state with clear visual indicators to the user.

### Rule 2: Cryptographic Serialization Moulding
- **IF Profile contains multi-platform synchronization (e.g. Dart $\leftrightarrow$ TypeScript):**
  - Standard `JSON.stringify()` is **strictly prohibited** for signed payloads.
  - The agent must enforce **RFC 8785 Canonical JSON** with recursive alphabetical key sorting and normalized float precision across all client and backend layers.

### Rule 3: Database & RLS Access Moulding
- **IF Profile transitions from Local-Only to Cloud-Connected:**
  - The agent must immediately trigger the **Live SQL & Environment Safeguard Protocol** (`09_LIVE_DATABASE_MIGRATION_PROTOCOL.md`).
  - No anonymous read access may be granted to tables containing citizen or customer PII.
  - Telemetry and public kiosk heartbeat records must be segregated from user records to prevent PostgREST 401 conflict errors.
