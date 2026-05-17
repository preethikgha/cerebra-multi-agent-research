import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def search_web(query: str) -> list[dict]:
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )
    results = []
    for r in response["results"]:
        results.append({
            "title": r["title"],
            "url": r["url"],
            "content": r["content"]
        })
    return results