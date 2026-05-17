from typing import TypedDict, List
from langgraph.graph import StateGraph, END

class ResearchState(TypedDict):
    query: str                    
    search_results: List[dict]   
    critique: str                
    gaps: List[str]              
    needs_reresearch: bool        
    final_report: str            
    iteration: int                

def create_graph():
    from agents.researcher import researcher_node
    from agents.critic import critic_node
    from agents.synthesizer import synthesizer_node

    graph = StateGraph(ResearchState)

    graph.add_node("researcher", researcher_node)
    graph.add_node("critic", critic_node)
    graph.add_node("synthesizer", synthesizer_node)

   
    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "critic")

    graph.add_conditional_edges(
        "critic",
        lambda state: "researcher" if state["needs_reresearch"] and state["iteration"] < 2 else "synthesizer"
    )

    graph.add_edge("synthesizer", END)

    return graph.compile()
