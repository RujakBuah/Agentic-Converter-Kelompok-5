# Generated LangGraph Framework
# Source: aggregator.rdf
# System: AgenticSystem

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def aggregator_node_node(state: GraphState):
    # Original Logic: lambda x: x
    print(f"   [ACT] Node 'aggregator_node' is working...")
    new_msg = f"Processed by aggregator_node"
    return {"messages": [new_msg]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('aggregator_node', aggregator_node_node)
workflow.add_edge('aggregator_node', END)

workflow.add_edge(START, 'aggregator_node')

app = workflow.compile()
print(f"LangGraph 'AgenticSystem' compiled.")


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

