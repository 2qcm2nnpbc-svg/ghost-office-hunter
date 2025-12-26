import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import registry_researcher_agent
from tasks import investigation_task

# --- THE FIX: Import BaseTool from the CORE library ---
from crewai.tools import BaseTool 
from duckduckgo_search import DDGS

load_dotenv()

# --- Custom Tool Definition ---
# In main.py
class GhostHunterSearchTool(BaseTool):
    name: str = "Ghost Hunter Search"
    description: str = "Search the web for company addresses, news, and directors. Useful for finding red flags."

    def _run(self, query: str) -> str:
        try:
            # INCREASED max_results to 10 to catch the scandal news
            results = DDGS().text(keywords=query, region='wt-wt', safesearch='moderate', max_results=10)
            return str(results)
        except Exception as e:
            return f"Search failed: {e}"

# 1. Setup Tools
search_tool = GhostHunterSearchTool()

# 2. Setup Agent & Task
investigator = registry_researcher_agent()
investigator.tools = [search_tool]

# Target Company
target_company = "Three Arrows Capital" 

task1 = investigation_task(investigator, target_company)

# 3. Assemble Crew
crew = Crew(
    agents=[investigator],
    tasks=[task1],
    verbose=True,
    process=Process.sequential
)

# 4. Kickoff
print(f"Starting investigation into {target_company}...")
result = crew.kickoff()

# 5. Save the Evidence
with open("Three_Arrows_Forensic_Report.md", "w") as f:
    f.write(str(result))

print("\n\n######################")
print("✅ REPORT GENERATED: Three_Arrows_Forensic_Report.md")
print("######################")