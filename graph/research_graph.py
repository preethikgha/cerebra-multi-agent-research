from typing import TypedDict, List
from langgraph.graph import StateGraph, END

# This is the shared memory all agents read and write
class ResearchState(TypedDict):
    query: str                    # the user's question
    search_results: List[dict]    # raw results from Tavily
    critique: str                 # critic's feedback
    gaps: List[str]               # missing topics critic found
    needs_reresearch: bool        # should we search again?
    final_report: str             # synthesizer's output
    iteration: int                # how many search loops done

def create_graph():
    from agents.researcher import researcher_node
    from agents.critic import critic_node
    from agents.synthesizer import synthesizer_node

    graph = StateGraph(ResearchState)

    # Add all agents as nodes
    graph.add_node("researcher", researcher_node)
    graph.add_node("critic", critic_node)
    graph.add_node("synthesizer", synthesizer_node)

    # Define the flow
    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "critic")

    # Critic decides: re-search or move to synthesizer
    graph.add_conditional_edges(
        "critic",
        lambda state: "researcher" if state["needs_reresearch"] and state["iteration"] < 2 else "synthesizer"
    )

    graph.add_edge("synthesizer", END)

    return graph.compile()