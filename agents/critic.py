import os
import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

def critic_node(state: dict) -> dict:
    query = state["query"]
    results = state["search_results"]

    sources_text = "\n\n".join([
        f"Title: {r['title']}\nContent: {r['content']}"
        for r in results
    ])

    prompt = f"""You are a critical research analyst.

Query: {query}

Sources collected:
{sources_text}

Analyze these sources and respond ONLY with a JSON object, nothing else:
{{
    "critique": "your overall critique of the sources",
    "gaps": ["gap1", "gap2"],
    "needs_reresearch": true or false
}}"""

    response = llm.invoke(prompt)
    
    try:
        text = response.content.strip()
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        parsed = json.loads(text.strip())
    except:
        parsed = {
            "critique": response.content,
            "gaps": [],
            "needs_reresearch": False
        }

    return {
        **state,
        "critique": parsed.get("critique", ""),
        "gaps": parsed.get("gaps", []),
        "needs_reresearch": parsed.get("needs_reresearch", False)
    }