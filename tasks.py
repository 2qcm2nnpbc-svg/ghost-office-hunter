"""Task definitions for Ghost Office Hunter."""
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