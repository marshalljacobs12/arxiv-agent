from crewai import Task
from agents.research_agent import researcher

research_task = Task(
    description = (" Find the top 10 research papers from the search results from arXiv on {date}."),
    expected_output = (
        "A list of top 10 research papers with the following information in the following format:"
        "- Title"
        "- Authors"
        "- Abstract"
        "- Link to the paper"
    ),
    agent = researcher,
    human_input = True,
)
   