# Generated LangGraph Framework
# Source: router.ttl
# System: Router

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def router_node(state: GraphState):
    # Original Logic: Execute router_node
    print(f"   [ACT] Node 'router_node' is working...")
    return {"messages": ["Processed by router_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('router_node', router_node)
workflow.add_edge(START, 'router_node')
workflow.add_edge('router_node', END)

app = workflow.compile()
print(f"LangGraph 'Router' compiled.")


if __name__ == "__main__":
    try:
        print("Build success. Generating Mermaid Graph...")
        
        # 1. Print Mermaid Code (Text) - Tetap berguna untuk debugging/copy-paste
        try:
            mermaid_code = app.get_graph().draw_mermaid()
            print("\n--- MERMAID CODE (Copy to mermaid.live) ---")
            print(mermaid_code)
            print("-------------------------------------------\n")
        except Exception:
            print("[Info] Mermaid code generation failed (Graph might be empty).")

        # Catatan: Image generation sekarang ditangani oleh 'visualize_batch.py'

        print("\n--- Starting Simulation ---")
        initial_state = {"messages": ["START_SIGNAL"]}
        result = app.invoke(initial_state)
        print("\n--- Final State Content ---")
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}")

