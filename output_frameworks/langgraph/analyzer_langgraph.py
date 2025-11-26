# Generated LangGraph Framework
# Source: analyzer.ttl
# System: Analyzer

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def analyzer_node(state: GraphState):
    # Original Logic: Execute analyzer_node
    print(f"   [ACT] Node 'analyzer_node' is working...")
    return {"messages": ["Processed by analyzer_node"]}

def analyze_node(state: GraphState):
    # Original Logic: Execute analyze_node
    print(f"   [ACT] Node 'analyze_node' is working...")
    return {"messages": ["Processed by analyze_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('analyzer_node', analyzer_node)
workflow.add_node('analyze_node', analyze_node)
workflow.add_edge('analyzer_node', 'analyze_node')
workflow.add_edge(START, 'analyzer_node')
workflow.add_edge('analyze_node', END)

app = workflow.compile()
print(f"LangGraph 'Analyzer' compiled.")


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

