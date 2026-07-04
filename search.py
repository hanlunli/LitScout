import arxiv
from typing import List, Dict, Any

def search_arxiv(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """
    Search arxiv for the given query and return a list of dictionaries containing paper details.
    """
    client = arxiv.Client()
    # Disable SSL verification for this session
    client._session.verify = False
    
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []
    for paper in client.results(search):
        results.append({
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "published": paper.published.strftime("%Y-%m-%d"),
            "summary": paper.summary,
            "url": paper.entry_id
        })
    
    return results
