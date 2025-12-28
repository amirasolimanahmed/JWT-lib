

# 🔐 JWT Security Testing Library for Robot Framework

## Overview

This repository provides a **Python-based JWT security testing library** designed to be used with **Robot Framework**.
It enables security testers, QA engineers, and DevSecOps teams to **validate JSON Web Token (JWT) implementations against real-world attack scenarios**, aligned with **OWASP API Security Top 10** and **ISO/IEC 27001:2022**.

The library leverages **MyJWT** to automate common JWT vulnerability checks without relying on CLI execution, making it suitable for **CI/CD pipelines** and **BDD-style security testing**.

---

## 📘 Introduction to JSON Web Tokens

A **JSON Web Token (JWT)** is an open standard (RFC 7519) that defines a compact, self-contained mechanism for securely transmitting information between parties as a JSON object. JWTs are digitally signed, ensuring authenticity and integrity.

JWTs can be signed using:

* A shared secret (**HMAC**), or
* A public/private key pair (**RSA** or **ECDSA**)

More details: [https://jwt.io/introduction](https://jwt.io/introduction)

---

## 🧱 JWT Structure

A JWT consists of three Base64URL-encoded parts separated by dots (`.`):

1. **Header** – Token type and signing algorithm
2. **Payload** – Claims (identity, roles, permissions, metadata)
3. **Signature** – Integrity and authenticity protection

---

## 🎯 When to Use JWTs

### Authorization

JWTs are commonly used for stateless authentication and authorization. Once issued, the token is sent with every request to protected endpoints, enabling scalable and decoupled security.

### Secure Information Exchange

JWTs ensure that transmitted claims are verifiable and tamper-proof through cryptographic signatures.

---

## 🧪 Library Capabilities

This library exposes **Robot Framework keywords** that automate JWT security testing scenarios, including:

* JWT modification and re-signing
* `none` algorithm abuse
* Weak secret brute forcing
* RSA/HMAC algorithm confusion
* `kid` header injection
* `jku` and `x5u` URL-based key injection
* Sending modified JWTs to target endpoints

---

## 📦 Installation

### Prerequisites

```bash
pip install myjwt
```

---

## ⚙️ Robot Framework Setup

Add the JWT library to your Robot Framework test suite:

```robot
*** Settings ***
Library    ../Libraries/jwt.py
```

---

## 🤖 Robot Framework Example Test Cases

### 1️⃣ None Algorithm Vulnerability Test

**OWASP API2 – Broken Authentication**

```robot
*** Test Cases ***
JWT None Algorithm Attack
    ${jwt}=    Load Original JWT    valid_jwt.txt
    ${modified}=    Modify JWT Algorithm    ${jwt}    none
    ${response}=    Send JWT To URL    ${modified}    https://api.example.com/protected
    Should Be Equal As Integers    ${response.status_code}    401
```

---

### 2️⃣ RSA / HMAC Confusion Attack

**OWASP API2 – Broken Authentication**

```robot
*** Test Cases ***
JWT RSA HMAC Confusion
    ${jwt}=    Load Original JWT    rsa_signed_jwt.txt
    ${modified}=    Perform RSA HMAC Confusion    ${jwt}    public.pem
    ${response}=    Send JWT To URL    ${modified}    https://api.example.com/protected
    Should Be Equal As Integers    ${response.status_code}    401
```

---

### 3️⃣ `kid` Injection Attack

**OWASP API8 – Security Misconfiguration**

```robot
*** Test Cases ***
JWT KID Injection
    ${jwt}=    Load Original JWT    valid_jwt.txt
    ${modified}=    Inject KID Header    ${jwt}    ../../../../etc/passwd
    ${response}=    Send JWT To URL    ${modified}    https://api.example.com/protected
    Should Not Be Equal As Integers    ${response.status_code}    200
```

---

## 🔗 OWASP API Security Top 10 Mapping

| JWT Vulnerability            | OWASP API Risk                             |
| ---------------------------- | ------------------------------------------ |
| `none` algorithm             | API2 – Broken Authentication               |
| Weak HMAC secrets            | API2 – Broken Authentication               |
| RSA/HMAC confusion           | API2 – Broken Authentication               |
| Missing signature validation | API2 – Broken Authentication               |
| `kid` injection              | API8 – Security Misconfiguration           |
| `jku` / `x5u` abuse          | API8 – Security Misconfiguration           |
| Unvalidated claims           | API5 – Broken Function Level Authorization |

---

## 🧩 ISO/IEC 27001:2022 Mapping

| JWT Risk                             | ISO Control                                 |
| ------------------------------------ | ------------------------------------------- |
| Weak token signing                   | A.8.24 – Cryptographic controls             |
| Broken authentication                | A.5.17 – Authentication information         |
| Token tampering                      | A.8.21 – Secure system architecture         |
| Misconfigured JWT validation         | A.8.20 – Network security                   |
| Untrusted key sources (`jku`, `x5u`) | A.5.23 – Information security for suppliers |
| Missing monitoring                   | A.8.16 – Monitoring activities              |

---

## 🚀 CI/CD & DevSecOps Usage

This library is ideal for:

* Security regression testing
* API pipeline security gates
* BDD-based security testing
* OWASP & ISO compliance evidence
* Shift-left security strategies

---

## 📚 References

* MyJWT Documentation: [https://myjwt.readthedocs.io/en/latest/](https://myjwt.readthedocs.io/en/latest/)
* MyJWT GitHub: [https://github.com/mBouamama/MyJWT](https://github.com/mBouamama/MyJWT)
* JWT Introduction: [https://jwt.io/](https://jwt.io/)
* OWASP API Security Top 10: [https://owasp.org/www-project-api-security/](https://owasp.org/www-project-api-security/)



Stay tuned 🚀

