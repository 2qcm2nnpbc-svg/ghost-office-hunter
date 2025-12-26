from crewai import Task

def investigation_task(agent, company_name):
    return Task(
        description=f"""
        conduct a forensic investigation on '{company_name}'.
        
        1. ADVERSE MEDIA CHECK: Search specifically for terms like "fraud", "collapse", "arrest", "investigation", "liquidators", "MAS penalty", and "bankruptcy" associated with the company or its directors (Su Zhu, Kyle Davies).
        2. GHOST OFFICE CHECK: Identify if their Singapore address ({company_name} Singapore) is a co-working space or shared office.
        
        CRITICAL: If you find ANY negative news, you MUST flag it as a HIGH RISK entity. Do not return a 'clean' report if the company has collapsed.
        """,
        expected_output="A forensic risk report highlighting any regulatory actions, arrests, or insolvency proceedings.",
        agent=agent
    )