# Generated LangGraph Framework
# Source: customer_support.rdf
# System: CustomerSupportSystem

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def supportagent_node(state: GraphState):
    # Original Logic: Handle customer inquiries
    print(f"   [ACT] Node 'supportagent' is working...")
    new_msg = f"Processed by supportagent"
    return {"messages": [new_msg]}

def escalationagent_node(state: GraphState):
    # Original Logic: Handle complex issues
    print(f"   [ACT] Node 'escalationagent' is working...")
    new_msg = f"Processed by escalationagent"
    return {"messages": [new_msg]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('supportagent', supportagent_node)
workflow.add_edge('supportagent', 'escalationagent')
workflow.add_node('escalationagent', escalationagent_node)
workflow.add_edge('escalationagent', END)

workflow.add_edge(START, 'supportagent')

app = workflow.compile()
print(f"LangGraph 'CustomerSupportSystem' compiled.")


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

