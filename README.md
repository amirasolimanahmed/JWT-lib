

# 🔐 JWT Security Testing Library for Robot Framework

## Overview

This repository provides a **Python-based JWT security testing library** designed for use with **Robot Framework**.
It enables **Security Testers, QA Engineers, and DevSecOps teams** to validate **JSON Web Token (JWT)** implementations against **real-world attack scenarios**.

The library supports:

* **Automated JWT security testing**
* **OWASP API Security Top 10 alignment**
* **ISO/IEC 27001:2022 Annex A mapping**
* **CI/CD & shift-left security**
* **BDD-friendly Robot Framework tests**

The implementation wraps **MyJWT** functionality in a **safe, reusable, and test-friendly way**, avoiding direct CLI usage in test cases.

---

## 📘 Introduction to JSON Web Tokens

A **JSON Web Token (JWT)** is an open standard (RFC 7519) that defines a compact and self-contained mechanism for securely transmitting information between parties as a JSON object.

JWTs are digitally signed to ensure **authenticity** and **integrity**, using:

* A shared secret (**HMAC**), or
* A public/private key pair (**RSA** or **ECDSA**)

📖 More details: [https://jwt.io/introduction](https://jwt.io/introduction)

---

## 🧱 JWT Structure

A JWT consists of three Base64URL-encoded parts separated by dots (`.`):

1. **Header** – Token type and signing algorithm
2. **Payload** – Claims (identity, roles, permissions, metadata)
3. **Signature** – Integrity and authenticity protection

---

## 🎯 When to Use JWTs

### Authorization

JWTs are commonly used for **stateless authentication and authorization**.
Once issued, the token is sent with each request to protected endpoints, enabling scalable and decoupled security.

### Secure Information Exchange

JWTs ensure transmitted claims are **verifiable and tamper-proof** through cryptographic signatures.

---

## 🧪 Library Capabilities

This library exposes **Robot Framework keywords** that automate JWT security testing scenarios, including:

* JWT modification and re-signing
* `none` algorithm abuse
* Weak HMAC secret brute forcing
* RSA / HMAC algorithm confusion
* `kid` header injection
* `jku` and `x5u` remote key injection
* Sending modified JWTs to target endpoints

---

## 📦 Installation

### Prerequisites

```bash
pip install robotframework
pip install myjwt
```

---

## 🗂️ Recommended Project Structure

```
jwt-security-tests/
│
├── libraries/
│   └── jwt.py                  # Refactored Python JWT library
│
├── resources/
│   └── jwt_keywords.robot      # Reusable Robot keywords
│
├── tests/
│   ├── jwt_none_algorithm.robot
│   ├── jwt_kid_injection.robot
│   └── jwt_rsa_hmac.robot
│
├── data/
│   ├── valid_jwt.txt
│   └── rsa_public.pem
│
└── reports/
    ├── report.html
    ├── log.html
    └── output.xml
```

---

## ⚙️ Robot Framework Setup

Add the JWT Python library to your test suite:

```robot
*** Settings ***
Library    ../libraries/jwt.py
Resource   ../resources/jwt_keywords.robot
```

---

## 🧩 Robot Resource Keywords

### `resources/jwt_keywords.robot`

```robot
*** Keywords ***
Load JWT From File
    [Arguments]    ${path}
    ${jwt}=    Get File    ${path}
    ${jwt}=    Strip String    ${jwt}
    [Return]    ${jwt}

JWT Should Be Rejected
    [Arguments]    ${result}
    Should Not Be Equal As Integers    ${result.returncode}    0
```

---

## 🤖 Robot Framework Example Test Cases

### 1️⃣ None Algorithm Vulnerability

**OWASP API2 – Broken Authentication**

```robot
*** Test Cases ***
JWT None Algorithm Must Be Rejected
    [Tags]    OWASP_API2    JWT
    ${jwt}=        Load JWT From File    ../data/valid_jwt.txt
    ${result}=     None Vulnerability    ${jwt}
    JWT Should Be Rejected               ${result}
```

---

### 2️⃣ RSA / HMAC Confusion

**OWASP API2 – Broken Authentication**

```robot
*** Test Cases ***
JWT RSA HMAC Confusion Attack
    [Tags]    OWASP_API2    JWT
    ${jwt}=        Load JWT From File    ../data/valid_jwt.txt
    ${result}=     Rsa Hmac Confusion    ${jwt}    ../data/rsa_public.pem
    JWT Should Be Rejected               ${result}
```

---

### 3️⃣ `kid` Injection

**OWASP API8 – Security Misconfiguration**

```robot
*** Test Cases ***
JWT KID Injection Attack
    [Tags]    OWASP_API8    JWT
    ${jwt}=        Load JWT From File    ../data/valid_jwt.txt
    ${result}=     Kid Injection         ${jwt}
    JWT Should Be Rejected               ${result}
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

| JWT Risk                             | ISO/IEC 27001:2022 Control          |
| ------------------------------------ | ----------------------------------- |
| Weak token signing                   | A.8.24 – Cryptographic controls     |
| Broken authentication                | A.5.17 – Authentication information |
| Token tampering                      | A.8.21 – Secure system architecture |
| Misconfigured JWT validation         | A.8.20 – Network security           |
| Untrusted key sources (`jku`, `x5u`) | A.5.23 – Supplier relationships     |
| Missing monitoring                   | A.8.16 – Monitoring activities      |

---

## 🚀 CI/CD & DevSecOps Usage

This library is ideal for:

* Security regression testing
* API security gates in CI/CD pipelines
* Shift-left security testing
* OWASP & ISO compliance evidence
* BDD-style security automation

Run all tests:

```bash
robot -d reports tests/
```

---

## 📚 References

* MyJWT Documentation: [https://myjwt.readthedocs.io/en/latest/](https://myjwt.readthedocs.io/en/latest/)
* MyJWT GitHub: [https://github.com/mBouamama/MyJWT](https://github.com/mBouamama/MyJWT)
* JWT Introduction: [https://jwt.io/](https://jwt.io/)
* OWASP API Security Top 10: [https://owasp.org/www-project-api-security/](https://owasp.org/www-project-api-security/)

