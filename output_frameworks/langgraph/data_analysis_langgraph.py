# Generated LangGraph Framework
# Source: data_analysis.ttl
# System: DataAnalysisTeam

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def analyst_node(state: GraphState):
    # Original Logic: Execute analyst
    print(f"   [ACT] Node 'analyst' is working...")
    return {"messages": ["Processed by analyst_node"]}

def visualizer_node(state: GraphState):
    # Original Logic: Execute visualizer
    print(f"   [ACT] Node 'visualizer' is working...")
    return {"messages": ["Processed by visualizer_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('analyst_node', analyst_node)
workflow.add_node('visualizer_node', visualizer_node)
workflow.add_edge('analyst_node', 'visualizer_node')
workflow.add_edge(START, 'analyst_node')
workflow.add_edge('visualizer_node', END)

app = workflow.compile()
print(f"LangGraph 'DataAnalysisTeam' compiled.")


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

