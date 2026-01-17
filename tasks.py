"""Task definitions for Ghost Office Hunter."""
from typing import Optional
from crewai import Agent, Task


def investigation_task(agent: Agent, company_name: str) -> Task:
    """
    Create an investigation task for a company.
    
    Args:
        agent: The agent assigned to this task
        company_name: Name of the company to investigate
        
    Returns:
        Configured Task instance
    """
    return Task(
        description=f"""
        Conduct a comprehensive forensic investigation on '{company_name}'.
        
        1. ADVERSE MEDIA CHECK: 
           - Search specifically for terms like "fraud", "collapse", "arrest", "investigation", 
             "liquidators", "MAS penalty", "bankruptcy", "sanctions", and "regulatory action" 
             associated with the company or its directors.
           - Look for any negative news, legal proceedings, or regulatory violations.
        
        2. GHOST OFFICE CHECK: 
           - Identify if the company's Singapore address is a co-working space, shared office, 
             or virtual office.
           - Verify physical presence and operational legitimacy.
           - Check for entity clustering (multiple unrelated companies at same address).
        
        3. CORPORATE STRUCTURE ANALYSIS:
           - Examine corporate registry data for red flags.
           - Identify shell company characteristics.
           - Assess operational transparency.
        
        CRITICAL: If you find ANY negative news, regulatory actions, or suspicious patterns, 
        you MUST flag it as a HIGH RISK entity. Do not return a 'clean' report if the company 
        has collapsed, is under investigation, or shows signs of being a shell company.
        """,
        expected_output=(
            "A comprehensive forensic risk report in markdown format that includes:\n"
            "- Executive summary with risk rating\n"
            "- Adverse media findings\n"
            "- Ghost office assessment\n"
            "- Corporate structure analysis\n"
            "- Recommendations and red flags\n"
            "- Supporting evidence and sources"
        ),
        agent=agent
    )


def shariah_compliance_task(agent: Agent, company_name: str, ticker_symbol: Optional[str] = None) -> Task:
    """
    Create a Shariah compliance check task for a company.
    
    Args:
        agent: The agent assigned to this task
        company_name: Name of the company to check
        ticker_symbol: Optional stock ticker symbol. If not provided, agent should search for it.
        
    Returns:
        Configured Task instance
    """
    ticker_instruction = (
        f"Use the ticker symbol '{ticker_symbol}' to check Shariah compliance."
        if ticker_symbol
        else "First, search for the company's stock ticker symbol, then use it to check Shariah compliance."
    )
    
    return Task(
        description=f"""
        Conduct a comprehensive Shariah compliance assessment for '{company_name}'.
        
        {ticker_instruction}
        
        Perform the following checks:
        
        1. FINANCIAL RATIOS CHECK (AAOIFI Standards):
           Use the Shariah Compliance Checker tool to evaluate:
           - DEBT RATIO: Calculate debt-to-market cap ratio and verify it is below 33% threshold
           - CASH RATIO: Calculate cash-to-market cap ratio and verify it is below 33% threshold
           - Flag if either ratio exceeds threshold
        
        2. BUSINESS ACTIVITY ANALYSIS:
           Use the Shariah Business Activity Analyzer tool to fetch the company's business summary.
           Then carefully analyze the business description for prohibited activities:
           
           CRITICAL PROHIBITED ACTIVITIES TO FLAG:
           - Alcohol: brewing, distilling, wine, spirits, beer, liquor, alcoholic beverages
           - Gambling: casinos, betting, lottery, gaming, wagering, gambling operations
           - Pork products: pork, bacon, ham, pork-based products, swine products
           - Adult entertainment: pornography, adult content, adult entertainment services
           - Interest-based income: riba, usury, conventional banking interest, interest income
           - Tobacco: cigarette manufacturing, tobacco products (if applicable)
           - Weapons: arms manufacturing, weapons trade (if applicable)
           
           If ANY of these prohibited activities are mentioned or implied in the business summary,
           the company MUST be flagged as NON-COMPLIANT for business activities, regardless of 
           financial ratios.
        
        3. OVERALL COMPLIANCE ASSESSMENT:
           - Determine PASS/FAIL status based on BOTH financial ratios AND business activities
           - A company must pass BOTH checks to be Shariah-compliant:
             * Financial ratios: Both debt and cash ratios must be below 33%
             * Business activities: No prohibited activities in business operations
           - Provide clear explanation of compliance status for each component
           - Include market capitalization information
           - If the company fails either check, clearly state which aspect failed
        
        Note: For a company to be Shariah-compliant, it must:
        1. Have both debt ratio AND cash ratio below 33% (AAOIFI standard)
        2. NOT engage in prohibited business activities (alcohol, gambling, pork, adult entertainment, interest-based income, etc.)
        """,
        expected_output=(
            "A comprehensive Shariah compliance report in markdown format that includes:\n"
            "- Company name and ticker symbol\n"
            "- Overall compliance status (PASS/FAIL)\n"
            "- Financial Ratios Section:\n"
            "  * Debt ratio analysis with threshold comparison\n"
            "  * Cash ratio analysis with threshold comparison\n"
            "  * Market capitalization information\n"
            "- Business Activity Analysis Section:\n"
            "  * Business summary overview\n"
            "  * Analysis of prohibited activities (if any found)\n"
            "  * Business activity compliance status\n"
            "- Overall Assessment:\n"
            "  * Clear explanation of compliance status for both financial and business aspects\n"
            "  * Specific reasons for PASS/FAIL status\n"
            "  * Recommendations if the company fails compliance"
        ),
        agent=agent
    )