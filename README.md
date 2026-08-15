# 📂 File Feed Agent — AI-Powered Data Ingest Monitor

> **An autonomous AI monitoring agent that watches, validates, and routes data files**  
> Acts as the first line of defense for critical data pipelines.

---

## ❌ The Problem

In TPA/Payer environments, thousands of files arrive daily — 834s, 837s, eligibility files, claims feeds. Staff must manually check SFTP folders hourly, identify file types, validate formats, and route them for processing. Files get stuck in inboxes, naming conventions drift, and missed files mean missed SLAs, delayed claims, and compliance violations.

**Before:** Manual hourly folder checks, stuck/lost files, human error, missed SLAs, staff burnout.

**After (AI Agent):** 24/7 autonomous monitoring — instant file detection, pattern recognition, validation routing, and email alerts for anomalies. Zero missed files, SLA compliance guaranteed.

---

## 🧠 AI Agent Architecture

```mermaid
graph TB
    subgraph INPUT["📥 Inbound Data Layer"]
        I1[SFTP Drop Zone]
        I2[Email Attachments]
        I3[API Webhook]
    end

    subgraph AGENT["🤖 File Feed Agent Core"]
        A1[Watcher Agent\nContinuous Polling]
        A2[Pattern Recognition\nAgent]
        A3[Validation Rules\nAgent]
        A4[Routing Decision\nAgent]
    end

    subgraph OUTCOMES["📤 Action Layer"]
        O1[Processed Queue\nValid Files]
        O2[Error Queue\nInvalid Files]
        O3[Alert Queue\nUnknown Files]
    end

    subgraph HUMAN["👤 Human Oversight"]
        H1[Operator Dashboard]
        H2[Email Notifications]
        H3[Activity Log]
    end

    I1 --> A1
    I2 --> A1
    I3 --> A1
    A1 -->|File Detected| A2
    A2 -->|Pattern Match| A3
    A3 -->|Valid| A4
    A3 -->|Invalid| O2
    A3 -->|Unknown| O3
    A4 --> O1
    O1 --> H1
    O2 --> H1
    O3 -->|EMAIL SENT| H2
    A1 --> H3

    style A1 fill:#4CAF50,stroke:#333,color:#fff
    style A2 fill:#2196F3,stroke:#333,color:#fff
    style A3 fill:#FF9800,stroke:#333,color:#fff
    style A4 fill:#9C27B0,stroke:#333,color:#fff
```

## 🤖 How the AI Agent Works

This is an **autonomous file monitoring agent** that never sleeps:

| Agent Component | Function |
|----------------|----------|
| **Watcher Agent** | Continuously polls input directories — zero-latency file detection |
| **Pattern Recognition Agent** | Uses `fnmatch` to match files against configurable glob patterns (CLAIMS_*.csv, ENROLL_*.csv) |
| **Validation Rules Agent** | Checks header integrity, file size thresholds, naming conventions |
| **Routing Decision Agent** | Moves valid files → `processed/`, invalid → `errors/`, unknown → alerts |
| **Alerting Agent** | Sends email-style notifications for anomalous file events |

## 🔄 Before vs After

```mermaid
graph LR
    subgraph BEFORE["❌ Before (Manual)"]
        BM[Staff manually check\nSFTP folders hourly\nFiles get stuck/lost\nMissed SLAs]
    end

    subgraph AFTER["✅ After (AI Agent)"]
        AM[24/7 autonomous monitoring\nInstant file routing\nZero missed files\nSLA compliance]
    end

    BM -->|File Feed Agent| AM
```

## 🛠 Tech Stack

| Component | Technology | Agent Role |
|-----------|-----------|------------|
| **Core Logic** | Python 3.10+ | Agent brain |
| **Pattern Matching** | `fnmatch` | Recognition engine |
| **File Operations** | `shutil` | Atomic moves & routing |
| **Architecture** | Event-Loop (Daemon-ready) | Continuous operation |

## ⚡ Quick Start

```bash
# 1. Start the monitoring agent
python monitor.py
# Output: "Monitoring: ./input_feed"

# 2. Simulate file drops (in another terminal)
python test_feed.py

# 3. Check results
# Valid files → ./processed/
# Invalid files → ./errors/
# Alerts → activity.log
```

## 💡 Why This Matters

In TPA/Payer environments, thousands of files arrive daily (834s, 837s, Eligibility). A missing file can mean:
- Missed coverage enrollment
- Delayed claims processing
- Compliance violations

This AI agent acts as the **First Line of Defense** — ensuring no file is left stuck in an inbox.

---

Built by **[Shazaly Musa](https://github.com/SparkSpheartech)** — Founder, SparkSphear Tech  
*AI Agents for Healthcare Data Pipeline Automation*