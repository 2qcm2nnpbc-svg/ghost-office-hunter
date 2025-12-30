# 👻 Ghost Office Hunter (AI Compliance Agent)

## Demo
<p align="center">
  <video src="https://github.com/user-attachments/assets/de746eae-35a6-493a-960a-5724a1322ee6" width="100%" controls muted>
    Your browser does not support the video tag.
  </video>
</p>

## 🚀 Project Overview
An autonomous AI Agent designed to detect "Ghost Offices" and shell companies in Singapore. Built using **CrewAI** and **Python**, this tool automates the forensic investigation process often used in AML (Anti-Money Laundering) compliance.

## 🛠 Tech Stack
- **Framework:** CrewAI (Agentic Orchestration)
- **Search Logic:** Custom DuckDuckGo Tool (Adverse Media & Registry Scraping)
- **Language:** Python 3.12
- **Logic:** ReAct Pattern (Reason + Act)

## 🔍 Capability
The agent performs a 3-step forensic loop:
1.  **Address Verification:** Checks if the registered address is a known co-working space.
2.  **Entity Clustering:** Detects if multiple unrelated firms share the same unit number.
3.  **Adverse Media Check:** Scans for regulatory bans, arrests, or insolvency proceedings (e.g., Three Arrows Capital case study).

## ⚠️ Disclaimer
This is a proof-of-concept for educational and portfolio purposes.
