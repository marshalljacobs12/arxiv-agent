from crewai import Task
from tasks.research_task import research_task
from agents.frontend_agent import frontend_engineer

reporting_task = Task(
    description = ("Compile the results into a detailed report in a HTML file."),
    expected_output = (
        "An HTML file with the results in the following format:"
        "Top 10 AI Research Papers published on {date}"
        "Use the tabular format for the following:"
        "- Title (which on clicking opens the paper in a new tab)"
        "- Authors"
        "- Short summary of the abstract (2-4 sentences)"
        "Please do not add '''html''' to the top and bottom of the final file."
    ),
    agent = frontend_engineer,
    context = [research_task],
    output_file = "./ai_research_report.html",
    human_input = True,
)
    