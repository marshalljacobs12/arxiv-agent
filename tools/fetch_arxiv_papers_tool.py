from typing import Type, List
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
import arxiv
import datetime
import time

class FetchArxivPapersInput(BaseModel):
    """Input schema for FetchArxivPapersTool."""
    target_date: datetime.date = Field(..., description="Target date to fetch papers for.")

class FetchArxivPapersTool(BaseTool):
    name: str = "fetch_arxiv_papers"
    description: str = "Fetches all arXiv papers from selected categories submitted on the target date."
    args_schema: Type[BaseModel] = FetchArxivPapersInput

    def _run(self, target_date: datetime.date) -> List[dict]:
        # List of AI-related categories
        AI_CATEGORIES = ["cs.AI"]

        # Define the date range for the target date
        start_date = target_date.strftime('%Y%m%d%H%M')
        end_date = (target_date + datetime.timedelta(days=1)).strftime('%Y%m%d%H%M')

        # Initialize the arXiv client
        client = arxiv.Client(
            page_size=100,  # Fetch 100 results per page
            delay_seconds=3  # Delay between requests to respect rate limits
        )

        all_papers = []

        for category in AI_CATEGORIES:
            print(f"Fetching papers for category: {category}")

            search_query = f"cat:{category} AND submittedDate:[{start_date} TO {end_date}]"

            search = arxiv.Search(
                query=search_query,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                max_results=None  # Fetch all results
            )

            # Collect results for the category
            category_papers = []
            for result in client.results(search):
                category_papers.append({
                    'title': result.title,
                    'authors': [author.name for author in result.authors],
                    'summary': result.summary,
                    'published': result.published,
                    'url': result.entry_id
                })

                # Delay between requests to respect rate limits
                time.sleep(3)

            print(f"Fetched {len(category_papers)} papers from {category}")
            all_papers.extend(category_papers)

        return all_papers