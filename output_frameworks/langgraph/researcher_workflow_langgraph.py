# Generated LangGraph Framework
# Source: researcher_workflow.ttl
# System: ResearchWorkflow

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def researcher_node(state: GraphState):
    # Original Logic: Execute researcher
    print(f"   [ACT] Node 'researcher' is working...")
    return {"messages": ["Processed by researcher_node"]}

def writer_node(state: GraphState):
    # Original Logic: Execute writer
    print(f"   [ACT] Node 'writer' is working...")
    return {"messages": ["Processed by writer_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('researcher_node', researcher_node)
workflow.add_node('writer_node', writer_node)
workflow.add_edge('researcher_node', 'writer_node')
workflow.add_edge(START, 'researcher_node')
workflow.add_edge('writer_node', END)

app = workflow.compile()
print(f"LangGraph 'ResearchWorkflow' compiled.")


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

