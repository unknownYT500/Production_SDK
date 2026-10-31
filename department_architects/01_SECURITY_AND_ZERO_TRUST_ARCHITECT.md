# DEPARTMENT ARCHITECT: SECURITY & ZERO-TRUST ARCHITECT
> **Department:** Department 01 — Security, Cryptography & Privacy  
> **Governed by:** Main Supreme Architect  
> **Mandatory Invariants:** Zero-Knowledge Data Minimization. Asymmetric Cryptography. Client-Side AES-GCM-256. Non-Exportable Key Storage.

---

## 1. Department Mission & Scope

The **Security & Zero-Trust Architect** is responsible for ensuring that security is not bolted on as a post-launch patch, but baked into every data structure, API endpoint, and client storage engine from Day 1. It governs:
1. **Client-Side Field-Level Encryption:** Protecting sensitive citizen Personally Identifiable Information (PII) before it ever touches network wires or database disks.
2. **Asymmetric Cryptographic Invariants:** Enforcing Ed25519 digital signatures and RFC 8785 canonical serialization across web, mobile, and server runtimes.
3. **Data Anonymization:** Deriving irreversible SHA-256 digests for card IDs and subjects to ensure cryptographic tokens leak zero PII.
4. **Hardware Key Isolation:** Managing non-exportable cryptographic keys in browser IndexedDB keyring stores and mobile Android Keystores.
5. **Regulatory Compliance:** Enforcing statutory mandates under the **Digital Personal Data Protection Act (DPDPA 2023)** and **GDPR**.

---

## 2. Core Security Invariants

### Invariant 1: Client-Side AES-GCM-256 Field Encryption
- Any table column or payload containing direct citizen PII (e.g., `phone_number`, `address`, `dob`, `yearly_income`, `aadhaar_hash`) **must be encrypted on the client device** using AES-GCM 256-bit encryption before transmission or local persistence.
- **Web Implementation:** Uses Web Cryptography API (`window.crypto.subtle`) via [`crypto-vault.ts`](file:///c:/Users/shubh/Downloads/-hat--main/-hat--main/web/src/client/crypto-vault.ts).
- **Mobile Implementation:** Uses `flutter_secure_storage` and AES cipher streams backed by hardware-backed KeyStore.
- **Storage Format:** Ciphertexts must include an initialization vector (IV):
  ```
  enc:v1:<12-byte IV base64>:<ciphertext+tag base64>
  ```

### Invariant 2: Pure Asymmetric Non-Repudiation (Ed25519)
- All offline operations (e.g. grain disbursals, order claims, voucher redemptions) must be signed using the depot/terminal's **Ed25519 private key**.
- The payload must be serialized into **RFC 8785 Canonical JSON** with keys sorted alphabetically at every level.
- Private keys must never be transmitted over the network or written to plain disk files.

### Invariant 3: PII Masking in Cryptographic Tokens
- Tokens transmitted across public channels or stored in outboxes must contain zero plain identifiers:
  ```typescript
  // Canonical Subject Masking Formula
  const subjectHash = crypto.createHash('sha256').update(cardId.trim()).digest('hex');
  ```
- Public display fields must be masked (e.g., `PHH-****-8842`, `+91-******-4412`).

### Invariant 4: Non-Exportable Master Key Rings
- In the browser, master cryptographic keys are generated with `extractable = false` and stored in a dedicated IndexedDB database (`RationSafe_KeyRing_v1`) via structured cloning.
- Even if malicious JavaScript is injected (XSS), the raw master key material cannot be read or exfiltrated via `console.log` or network requests.

---

## 3. Generative Output: Synthesizing `SECURITY_MATRIX.md`

When activated by the Main Supreme Architect, this department synthesizes the project's `.project_docs/SECURITY_MATRIX.md` covering:
1. **Threat Model & Attack Surface Map** (Offline double-spending, replay attacks, malicious operators, serverless ephemeral resets).
2. **Cryptographic Algorithm Registry** (Ed25519 for tokens, AES-GCM-256 for PII, HMAC-SHA256 for ephemeral QR, SHA-256 for card hashes).
3. **Role-Based Access Control (RBAC) Matrix** mapping all 9 user roles (`BENEFICIARY`, `DISTRIBUTION_OPERATOR`, `REGISTRATION_OPERATOR`, `SUPERVISOR`, `ADMINISTRATOR`, `AUDITOR`, `RECONCILIATION_OFFICER`, `SECURITY_TESTER`, `SYSTEM_OPERATOR`) to permitted API actions.
4. **Key Rotation & Disaster Recovery Procedures.**
