from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

def registry_researcher_agent():
    return Agent(
        role='Corporate Registry Investigator',
        goal='Trace corporate structures and identify shell company characteristics',
        backstory="""You are an expert forensic analyst for a top-tier Singapore compliance firm. 
        Your specialty is 'Ghost Offices'—companies that exist only on paper. 
        You scrutinize corporate registry data for red flags.""",
        verbose=True,
        allow_delegation=False,
        tools=[] 
    )