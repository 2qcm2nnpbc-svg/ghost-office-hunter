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