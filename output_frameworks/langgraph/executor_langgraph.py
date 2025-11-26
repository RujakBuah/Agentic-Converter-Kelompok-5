# Generated LangGraph Framework
# Source: executor.ttl
# System: Executor

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def executor_node(state: GraphState):
    # Original Logic: Execute executor_node
    print(f"   [ACT] Node 'executor_node' is working...")
    return {"messages": ["Processed by executor_node"]}

def executorr_node(state: GraphState):
    # Original Logic: Execute executorr_node
    print(f"   [ACT] Node 'executorr_node' is working...")
    return {"messages": ["Processed by executorr_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('executor_node', executor_node)
workflow.add_node('executorr_node', executorr_node)
workflow.add_edge('executor_node', 'executorr_node')
workflow.add_edge(START, 'executor_node')
workflow.add_edge('executorr_node', END)

app = workflow.compile()
print(f"LangGraph 'Executor' compiled.")


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

