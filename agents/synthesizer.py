import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

def synthesizer_node(state: dict) -> dict:
    query = state["query"]
    results = state["search_results"]
    critique = state["critique"]

    sources_text = "\n\n".join([
        f"Source: {r['title']}\nURL: {r['url']}\nContent: {r['content']}"
        for r in results
    ])

    prompt = f"""You are an expert research synthesizer.

Query: {query}

Sources:
{sources_text}

Critic feedback:
{critique}

Write a comprehensive, well-structured research report that:
1. Directly answers the query
2. Cites sources by their title
3. Acknowledges any limitations noted by the critic
4. Uses clear headings and bullet points"""

    response = llm.invoke(prompt)

    return {
        **state,
        "final_report": response.content
    }