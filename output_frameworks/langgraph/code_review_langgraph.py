# Generated LangGraph Framework
# Source: code_review.rdf
# System: CodeReviewSystem

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def reviewer_node(state: GraphState):
    # Original Logic: Review code for quality and best practices
    print(f"   [ACT] Node 'reviewer' is working...")
    new_msg = f"Processed by reviewer"
    return {"messages": [new_msg]}

def tester_node(state: GraphState):
    # Original Logic: Generate and run tests
    print(f"   [ACT] Node 'tester' is working...")
    new_msg = f"Processed by tester"
    return {"messages": [new_msg]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('reviewer', reviewer_node)
workflow.add_edge('reviewer', 'tester')
workflow.add_node('tester', tester_node)
workflow.add_edge('tester', END)

workflow.add_edge(START, 'reviewer')

app = workflow.compile()
print(f"LangGraph 'CodeReviewSystem' compiled.")


if __name__ == "__main__":
    try:
        print("Build success. Visualizing Graph...")
        try:
            print(app.get_graph().draw_ascii())
        except Exception as e:
            print(f"[Info] Visualisasi Gagal: {e}")

        print("\n--- Starting Simulation ---")
        initial_state = {"messages": ["START_SIGNAL"]}
        result = app.invoke(initial_state)
        print("\n--- Final State Content ---")
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}")

