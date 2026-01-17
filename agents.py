"""Agent definitions for Ghost Office Hunter."""
from typing import List, Optional
from crewai import Agent
from crewai.tools import BaseTool


def registry_researcher_agent(
    tools: Optional[List[BaseTool]] = None,
    verbose: bool = True
) -> Agent:
    """
    Create a Corporate Registry Investigator agent.
    
    Args:
        tools: List of tools to assign to the agent
        verbose: Whether to enable verbose output
        
    Returns:
        Configured Agent instance
    """
    return Agent(
        role='Corporate Registry Investigator',
        goal='Trace corporate structures and identify shell company characteristics',
        backstory="""You are an expert forensic analyst for a top-tier Singapore compliance firm. 
        Your specialty is 'Ghost Offices'—companies that exist only on paper. 
        You scrutinize corporate registry data for red flags.""",
        verbose=verbose,
        allow_delegation=False,
        tools=tools or []
    )


def shariah_compliance_agent(
    tools: Optional[List[BaseTool]] = None,
    verbose: bool = True
) -> Agent:
    """
    Create a Shariah Compliance Analyst agent.
    
    Args:
        tools: List of tools to assign to the agent
        verbose: Whether to enable verbose output
        
    Returns:
        Configured Agent instance
    """
    return Agent(
        role='Shariah Compliance Analyst',
        goal='Evaluate companies against AAOIFI Shariah compliance standards using financial ratios and business activity analysis',
        backstory="""You are a specialized Islamic finance compliance expert working for a leading 
        Shariah-compliant investment firm. Your expertise lies in analyzing publicly traded companies 
        against AAOIFI (Accounting and Auditing Organization for Islamic Financial Institutions) 
        standards. You meticulously check:
        1. Financial ratios: debt ratios and cash ratios to ensure they are below 33% of market capitalization
        2. Business activities: company business descriptions for prohibited activities such as alcohol, 
           gambling, pork products, adult entertainment, and interest-based income (riba)
        
        You understand that for a company to be Shariah-compliant, it must:
        - Have both debt ratio AND cash ratio below 33% (AAOIFI standard)
        - NOT engage in prohibited business activities according to Islamic principles
        
        You are thorough and detail-oriented, carefully analyzing business summaries to identify any 
        mention or implication of prohibited activities that would make a company non-compliant.""",
        verbose=verbose,
        allow_delegation=False,
        tools=tools or []
    )