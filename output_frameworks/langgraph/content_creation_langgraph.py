# Generated LangGraph Framework
# Source: content_creation.ttl
# System: ContentCreationPipeline

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def ideator_node(state: GraphState):
    # Original Logic: Execute ideator
    print(f"   [ACT] Node 'ideator' is working...")
    return {"messages": ["Processed by ideator_node"]}

def writer_node(state: GraphState):
    # Original Logic: Execute writer
    print(f"   [ACT] Node 'writer' is working...")
    return {"messages": ["Processed by writer_node"]}

def editor_node(state: GraphState):
    # Original Logic: Execute editor
    print(f"   [ACT] Node 'editor' is working...")
    return {"messages": ["Processed by editor_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('ideator_node', ideator_node)
workflow.add_node('writer_node', writer_node)
workflow.add_node('editor_node', editor_node)
workflow.add_edge('ideator_node', 'writer_node')
workflow.add_edge('writer_node', 'editor_node')
workflow.add_edge(START, 'ideator_node')
workflow.add_edge('editor_node', END)

app = workflow.compile()
print(f"LangGraph 'ContentCreationPipeline' compiled.")


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

