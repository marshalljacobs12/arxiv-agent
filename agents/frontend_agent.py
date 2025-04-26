from crewai import Agent

frontend_engineer = Agent(
    role = "Senior Frontend & AI Engineer",
    goal = "Compile the results into a HTML file.",
    backstory = "You are a competent frontend engineer writing HTML and CSS with decades of experience."
                "You have also been working with AI for decades and understand it well",
    verbose = True,
)