# 👻 Ghost Office Hunter (AI Compliance Agent)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org)
[![Framework: CrewAI](https://img.shields.io/badge/Framework-CrewAI-red.svg)](https://crewai.com)
[![Field: AML/KYC](https://img.shields.io/badge/Field-Compliance%20/%20AML-green.svg)](https://en.wikipedia.org/wiki/Anti-money_laundering)

## 📺 Demo
<p align="center">
  <video src="https://github.com/user-attachments/assets/de746eae-35a6-493a-960a-5724a1322ee6" width="100%" controls muted autoplay>
    Your browser does not support the video tag.
  </video>
</p>

> **💡 Watch for Agentic Reasoning:** At **0:12**, the agent encounters a tool syntax error. Instead of crashing, it autonomously analyzes the failure, adjusts its query parameters, and retries the search—demonstrating true self-correction.

---

## 🚀 Project Overview
**Ghost Office Hunter** is an autonomous AI agent designed to flag high-risk "Ghost Offices" and shell companies within the Singapore business ecosystem. 

By automating the tedious process of manual registry cross-referencing and adverse media screening, this tool serves as a force multiplier for **AML (Anti-Money Laundering)** and **KYC (Know Your Customer)** compliance teams.



## 🛠 Tech Stack & Architecture
* **Orchestration:** [CrewAI](https://github.com/joaomdmoura/crewai) for multi-agent role-playing and task delegation.
* **Intelligence:** ReAct (Reason + Act) prompting pattern for complex decision-making.
* **Search Engine:** Custom-built `ddgs` (DuckDuckGo) tool for real-time web scraping without API costs.
* **Environment:** Python 3.12 (Optimized for M4 MacBook Pro execution).

## 🔍 Forensic Capabilities
The agent executes a sophisticated **Search-Verify-Report** loop:
1.  **Physical Presence Audit:** Differentiates between legitimate operational headquarters and "virtual office" hubs or high-density co-working spaces.
2.  **Entity Clustering:** Identifies "Red Flag" patterns where dozens of unrelated entities are registered to a single, unmanned unit.
3.  **Adverse Media Intelligence:** Performs deep-web scans for regulatory actions, bankruptcy filings, and leadership sanctions (e.g., the **Three Arrows Capital** forensic case study shown in the demo).

## 📥 Installation & Usage
1.  **Clone & Setup:**
    ```bash
    git clone [https://github.com/your-username/ghost-office-hunter.git](https://github.com/your-username/ghost-office-hunter.git)
    cd ghost-office-hunter
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
2.  **Execute:**
    ```bash
    # Run with warning suppression for a clean terminal output
    python -W ignore main.py
    ```

## ⚠️ Disclaimer
This project is a proof-of-concept developed for the **Agent AI** course completion (Dec 2025). It is intended for educational and portfolio demonstration purposes only.
