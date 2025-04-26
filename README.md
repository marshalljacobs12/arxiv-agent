# arxiv-agent

An **AI agent system** that automatically fetches, ranks, and compiles the top AI research papers from arXiv into an HTML report.

Built using [CrewAI](https://github.com/joaomdmoura/crewAI) agents and tools.

## Features

- ✨ **Research Agent**
  - Searches arXiv for AI papers submitted on a target date.
  - Selects the top 10 papers based on title and abstract.

- 📈 **Frontend Agent**
  - Takes the selected papers and formats them into a clean HTML report.

- 📂 **Modular Architecture**
  - Agents, Tasks, and Tools separated into clear modules for extensibility.

## Project Structure

```
.
├── agents/
│   ├── frontend_agent.py
│   └── research_agent.py
├── tasks/
│   ├── reporting_task.py
│   └── research_task.py
├── tools/
│   └── fetch_arxiv_papers_tool.py
├── main.py
├── README.md
```

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/marshalljacobs12/arxiv-agent.git
cd arxiv-agent
```

2. **Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

You also need an OpenAI API key set up via environment variables if your CrewAI agents require LLM calls (not configured yet, but recommended for future extensions).

4. **Run the Project**

```bash
python main.py
```

5. **Output**
- HTML report will be saved to `./ai_research_report.html`
- The final result will also print in the console.

## Dependencies
- Python 3.9+
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [arxiv Python API](https://lukasschwab.me/arxiv.py/)
- pydantic

## Notes
- Fetching papers can be slow because of arXiv rate limiting and the added intentional delays to avoid hitting API limits.
- This version currently fetches papers from category `cs.AI` only.
- Future extensions could add:
  - Multiple categories
  - Automatic summarization
  - Export to Markdown or PDF

## License
MIT License

---

Built with ❤️ by [Marshall Jacobs](https://github.com/marshalljacobs12).

