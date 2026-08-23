# 🏗️ Sepsis Monitor AI
## System Architecture & Engineering Documentation

---

# 📌 Executive Summary

The platform combines:

- Streamlit User Interface
- SQLAlchemy ORM
- SQLite Database
- Clinical Rules Engine
- AI Analysis Layer
- Promptfoo Validation
- GitHub Actions
- Docker Deployment

---
# 🏗️ High-Level Architecture

```text
┌────────────────────────────────────────────────────────┐
│               Streamlit Clinical UI                    │
└──────────────────────────┬─────────────────────────────┘
                           │ (Rerun Core Lifecycle)
                           ▼
┌────────────────────────────────────────────────────────┐
│             Clinical Orchestration (app.py)            │
└──────────────────────────┬─────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
┌────────────────┐ ┌───────────────┐ ┌───────────────┐
│Telemetry Engine│ │  AI Service   │ │  Guardrails   │
└────────┬───────┘ └───────┬───────┘ └───────┬───────┘
         │                 │                 │
         ▼                 ▼                 ▼
┌────────────────┐ ┌───────────────┐ ┌───────────────┐
│   SQLite DB    │ │   Groq LLM    │ │Prompt Filters │
└────────┬───────┘ └───────────────┘ └───────────────┘
         │
         ▼
┌────────────────┐
│Alembic Migrat. │
└────────────────┘
```

---

# 📂 Repository Structure

```text
Sepsis-Monitor-AI/

├── app.py
├── src/
├── tests/
├── assets/
├── database/
├── Dockerfile
├── promptfooConfig.yaml
├── pyproject.toml
└── README.md
```

---

# 🧠 Clinical Decision Engine

Inputs:

- Heart Rate
- Temperature
- Oxygen Saturation
- Blood Pressure
- CRP
- PCT
- Renal Status
- Kangaroo Care
- Music Therapy

---

# 🔬 Risk Classification

HIGH-RISK:

```text
PCT >= 0.5
OR
CRP >= 5.0
```

STABLE:

```text
PCT < 0.5
AND
CRP < 5.0
```

---

# 💊 Dose Engine

Ampicillin

```text
100 mg/kg/day
every 12h
```

Gentamicin

```text
4 mg/kg/day
daily
```

---
# 🛡️ Security Architecture

The application implements a defense-in-depth model across multiple system thresholds:
1. **Prompt Injection Detection:** Intercepts incoming telemetry strings at boundary execution limits.
2. **Regex Sanitization:** Scans, logs, and neutralizes hostile instruction override words.
3. **Structured Prompt Templates:** Context variables are isolated inside system-level tags.
4. **Promptfoo Red Team Validation:** Automated evaluations enforce boundary immune responses.
5. **Deterministic Medical Logic:** Micro-dosage calculators run natively in Python, immune to LLM manipulation.
6. **Clinical Guardrails:** Enforces post-inference verification on parsing block structures.

### Prompt Injection Detection Tokens Monitored:
- IGNORE
- OVERRIDE
- CLEAN
- SYSTEM RESET
- REVEAL
- PRINT

Detected attacks undergo immediate quarantining:
1. Flagged at application level
2. Logged via standard logger
3. Neutralized safely using placeholder text
4. Clinical analysis continues uninterrupted using safe rules

---

## 🧠 AI Architecture Philosophy

The AI subsystem is intentionally isolated from deterministic clinical calculations. Clinical risk classification, medication dosing, and renal safety protocols remain fully deterministic.

The AI layer is responsible for:
- Clinical report generation
- Medication explanations
- FCC evaluation
- Multilingual recommendations

The AI layer never modifies:
- Risk scores
- Drug dosages
- Safety thresholds
- AKI classifications

# 🤖 AI & Notification Pipeline

```text
Telemetry
   │
   ▼
Clinical Rules
   │
   ▼
Prompt Security ──► Local Terminal Alert (Bypass Live SMS)
   │
   ▼
Groq LLM
   │
   ▼
XML Output
   │
   ▼
Dashboard
```

# 📊 Validation Gallery

## Core Screens

01 Dashboard

02 Dose Calculation

03 Music Therapy

04 Clinical Analysis

05 Medication

06 FCC Evaluation

07 IDE Setup

---

## Cybersecurity Screens

08 Injection Alert

09 Security Sidebar

10 Payload Construction

---

## Clinical Scenarios

11-24 Standard Sepsis Workflow

25-29 Severe AKI Workflow

30 System Reset

---

# 🗄️ Database Architecture

Technology Stack:

- SQLite
- SQLAlchemy
- Alembic

Production Ready:

- PostgreSQL

---

# 📋 Telemetry Schema

| Column | Type |
|----------|----------|
| id | INTEGER |
| timestamp | TEXT |
| heart_rate | INTEGER |
| temperature | REAL |
| oxygen_saturation | INTEGER |
| blood_pressure | TEXT |
| crp | REAL |
| pct | REAL |
| weight | REAL |
| renal_status | TEXT |
| kangaroo_care | TEXT |
| music_therapy | TEXT |

---

# 🔄 Data Lifecycle

Execute Telemetry

```text
INSERT telemetry
COMMIT
REFRESH UI
```

Injection Therapy

```text
Recovery Values
INSERT telemetry
COMMIT
```

Reset

```sql
DELETE FROM telemetry;
VACUUM;
```

---

# ⚙️ CI/CD Pipeline

```text
Push
 │
 ▼
Ruff
 │
 ▼
Pytest
 │
 ▼
Promptfoo
 │
 ▼
Docker Build
 │
 ▼
PASS
```

---

# 🐳 Deployment

Development

- Streamlit
- SQLite

Production

- Docker
- PostgreSQL
- GitHub Actions

---

# 🎯 Engineering Highlights

- Clinical Decision Support
- AI-Assisted Analysis
- Prompt Security
- MLOps Validation
- Docker
- CI/CD
- Database Migrations