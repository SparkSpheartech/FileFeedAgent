# File Feed Command Center - Data Ingest Agent

**File Feed Command Center** is an automated monitoring agent designed to supervise critical data pipelines. It watches for incoming SFTP drops, validates file patterns against a rules engine, and routes them for processing—automatically triggering alerts for anomalies.

## 🚀 Key Features

*   **Real-time Monitoring**: Continuous polling loop watches input directories (0-latency detection).
*   **Rules Engine**: Use `config.json` to define complex file patterns (Globs) and map them to business actions.
*   **Automated Routing**: Automatically moves valid files to `processed/` and invalid files to `errors/`.
*   **Alerting System**: Integrated logging and mock-email notification system for "Unknown File" events.

## 🛠 Tech Stack
*   **Language**: Python 3.10+
*   **Core Logic**: `fnmatch` for pattern matching, `shutil` for atomic moves.
*   **Architecture**: Event-Loop Pattern (Daemon-ready).

## ⚡ How to Run

1.  **Start the Agent**:
    ```bash
    python monitor.py
    ```
    *The agent is now active. You will see "Monitoring: ./input_feed"*

2.  **Simulate File Drops**:
    Open a new terminal and run:
    ```bash
    python test_feed.py
    ```
    *This drops valid (CLAIMS, ENROLL) and invalid (UNKNOWN) files.*

3.  **Check Output**:
    *   **Valid Files** -> Moved to `./processed`
    *   **Bad Files** -> Moved to `./errors`
    *   **Logs** -> Check `activity.log` for "EMAIL SENT" alerts.

## 💡 Use Case
In TPA/Payer environments, thousands of files arrive daily (834s, 837s, Eligibility). A missing file can mean missed coverage. This agent acts as the **First Line of Defense**, ensuring no file is left stuck in an inbox.

---
*Created by Shazaly Musa*
