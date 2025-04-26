from crewai import Crew
from agents.research_agent import researcher
from agents.frontend_agent import frontend_engineer
from tasks.research_task import research_task
from tasks.reporting_task import reporting_task

arxiv_research_crew = Crew(
    agents = [researcher, frontend_engineer],
    tasks = [research_task, reporting_task],
    verbose = True,
)
     


crew_inputs = {
    "date" : "2025-04-24"
}
     

result = arxiv_research_crew.kickoff(inputs = crew_inputs)
print(result)