# 👻 Ghost Office Hunter (AI Compliance Agent)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org)
[![Framework: CrewAI](https://img.shields.io/badge/Framework-CrewAI-red.svg)](https://crewai.com)
[![Field: AML/KYC](https://img.shields.io/badge/Field-Compliance%20/%20AML-green.svg)](https://en.wikipedia.org/wiki/Anti-money_laundering)
[![Certification: Agentic AI](https://img.shields.io/badge/Certification-Reinvention%20with%20Agentic%20AI-blueviolet.svg)](https://www.credly.com/badges/5cc6097d-a216-42a4-8a26-793f1f8c0e40/public_url)

## 📺 Demo

Version 2: Enhancement - 10 Jan 2026
<p align="center">
  <video src="https://github.com/user-attachments/assets/a394e970-0a26-45df-bc48-09c4deab9c0b" width="100%" controls muted autoplay>
    Your browser does not support the video tag.
  </video>
</p>


Version 1: 
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
4.  **Shariah Compliance Check:** Evaluates publicly traded companies against AAOIFI (Accounting and Auditing Organization for Islamic Financial Institutions) standards by checking debt and cash ratios against the 33% threshold requirement.

## 📥 Installation & Usage

> **🚀 New to the project?** Check out the [Quick Start Guide](QUICKSTART.md) for a step-by-step walkthrough!

### Prerequisites
- Python 3.12 or higher
- OpenAI API key (required for CrewAI agents)

### Installation

#### Quick Setup (Recommended)

**On macOS/Linux:**
```bash
git clone https://github.com/your-username/ghost-office-hunter.git
cd ghost-office-hunter
./setup.sh
```

**On Windows:**
```cmd
git clone https://github.com/your-username/ghost-office-hunter.git
cd ghost-office-hunter
setup.bat
```

The setup script will:
- ✅ Check Python version (requires 3.12+)
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create `.env` file from template
- ✅ Create reports directory

#### Manual Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ghost-office-hunter.git
    cd ghost-office-hunter
    ```

2. **Create and activate virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    ```bash
    cp env.example .env
    # Edit .env and add your OPENAI_API_KEY
    ```

### Usage

#### Web UI (Recommended)

Launch the Streamlit web interface:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and use the interactive UI to:
- Enter company names
- Configure search settings
- Enable Shariah compliance checks (optional)
- View and download reports
- Monitor investigation progress

#### Command Line Interface

**Basic usage:**
```bash
python main.py "Company Name"
```

**With custom output path:**
```bash
python main.py "Company Name" --output custom_report.md
```

**With verbose logging:**
```bash
python main.py "Company Name" --verbose
```

**With Shariah compliance check:**
```bash
python main.py "Company Name" --shariah --ticker WTS
```

**Get help:**
```bash
python main.py --help
```

### Configuration

Edit `.env` file to customize configuration:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Model Configuration
OPENAI_MODEL_NAME=gpt-4
OPENAI_TEMPERATURE=0.7

# Optional: Search Configuration
SEARCH_MAX_RESULTS=10
SEARCH_REGION=wt-wt
SEARCH_SAFESEARCH=moderate

# Optional: Logging
LOG_LEVEL=INFO
LOG_FILE=ghost_office_hunter.log

# Optional: Output
OUTPUT_DIR=reports
```

### Output

Reports are saved to the `reports/` directory by default (configurable via `OUTPUT_DIR` environment variable). Each report is named `{Company_Name}_Forensic_Report.md`.

## 🕌 Shariah Compliance Feature

The Shariah compliance check evaluates publicly traded companies against **AAOIFI (Accounting and Auditing Organization for Islamic Financial Institutions)** standards using both financial ratios and business activity analysis.

### How It Works

The tool performs two comprehensive checks:

#### 1. Financial Ratios Check (AAOIFI Standards)

Checks two key financial ratios:

1. **Debt Ratio**: Total debt as a percentage of market capitalization
2. **Cash Ratio**: Total cash as a percentage of market capitalization

**Compliance Criteria:**
- Both ratios must be **below 33%** to PASS financial compliance
- If either ratio exceeds 33%, the company FAILS financial compliance

#### 2. Business Activity Analysis (LLM-Powered)

Uses an AI agent to analyze the company's business summary for prohibited activities:

**Prohibited Activities Checked:**
- 🍷 **Alcohol**: brewing, distilling, wine, spirits, beer, liquor, alcoholic beverages
- 🎰 **Gambling**: casinos, betting, lottery, gaming, wagering, gambling operations
- 🥓 **Pork Products**: pork, bacon, ham, pork-based products, swine products
- 🔞 **Adult Entertainment**: pornography, adult content, adult entertainment services
- 💰 **Interest-Based Income**: riba, usury, conventional banking interest, interest income
- 🚬 **Tobacco**: cigarette manufacturing, tobacco products (if applicable)
- 🔫 **Weapons**: arms manufacturing, weapons trade (if applicable)

**Compliance Criteria:**
- Company must **NOT engage in any prohibited activities** to PASS business activity compliance
- If any prohibited activities are found, the company FAILS business activity compliance

#### Overall Compliance Status

For a company to be **Shariah-compliant**, it must:
1. ✅ Pass financial ratios check (both debt and cash ratios < 33%)
2. ✅ Pass business activity check (no prohibited activities)

If either check fails, the company is **NON-COMPLIANT**.

### Usage Examples

**Command Line:**
```bash
# Check Shariah compliance for Watts Water Technologies
python main.py "Watts Water Technologies" --shariah --ticker WTS
```

**Web UI:**
1. Enter the company name
2. Check "Include Shariah Compliance Check" in Advanced Options
3. Enter the stock ticker symbol (e.g., WTS, AAPL, MSFT)
4. Run the investigation

### Data Source

The tool uses `yfinance` to fetch real-time financial data from Yahoo Finance, including:
- Market capitalization
- Total debt
- Total cash and cash equivalents
- Business summary and company description

**Note:** The ticker symbol must be valid and the company must be publicly traded for the Shariah compliance check to work.

### AI-Powered Analysis

The business activity analysis uses an **LLM (Large Language Model)** via CrewAI to:
- Read and understand the company's business summary
- Identify keywords and context related to prohibited activities
- Provide intelligent analysis beyond simple keyword matching
- Flag companies even if prohibited activities are mentioned indirectly

## 🏗️ Project Structure

```
ghost-office-hunter/
├── app.py               # Streamlit web UI
├── main.py              # Main entry point and CLI
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
├── tools.py             # Custom tools (search, etc.)
├── config.py            # Configuration management
├── logger.py            # Logging setup
├── requirements.txt     # Python dependencies
├── env.example          # Environment variables template
├── setup.sh             # Setup script (macOS/Linux)
├── setup.bat            # Setup script (Windows)
├── Makefile             # Make commands
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Development

### Code Quality
- Type hints throughout the codebase
- Comprehensive error handling
- Structured logging system
- Configuration management via environment variables

### Adding New Features
1. **New Agents**: Add to `agents.py`
2. **New Tasks**: Add to `tasks.py`
3. **New Tools**: Add to `tools.py`
4. **Configuration**: Update `config.py` and `env.example`

## 📝 License

This project is provided as-is for educational and demonstration purposes.

## ⚠️ Disclaimer
This project is a proof-of-concept developed for the **Agentic AI** course completion (Dec 2025). It is intended for educational and portfolio demonstration purposes only. 

**Important Notes:**
- Always verify AI-generated reports with human experts
- This tool is not a substitute for professional compliance review
- Results should be validated through official channels
- Use responsibly and in accordance with applicable laws and regulations
