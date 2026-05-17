import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools.search import search_web

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

def researcher_node(state: dict) -> dict:
    query = state["query"]
    
    if state.get("gaps"):
        gap_query = state["query"] + " " + " ".join(state["gaps"])
        results = search_web(gap_query)
    else:
        results = search_web(query)

    existing = state.get("search_results", [])
    
    return {
        **state,
        "search_results": existing + results,
        "iteration": state.get("iteration", 0) + 1
    }