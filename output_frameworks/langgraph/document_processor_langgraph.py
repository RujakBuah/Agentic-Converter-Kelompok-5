# Generated LangGraph Framework
# Source: document_processor.ttl
# System: DocumentProcessing

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def parser_node(state: GraphState):
    # Original Logic: Execute parser
    print(f"   [ACT] Node 'parser' is working...")
    return {"messages": ["Processed by parser_node"]}

def summarizer_node(state: GraphState):
    # Original Logic: Execute summarizer
    print(f"   [ACT] Node 'summarizer' is working...")
    return {"messages": ["Processed by summarizer_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('parser_node', parser_node)
workflow.add_node('summarizer_node', summarizer_node)
workflow.add_edge('parser_node', 'summarizer_node')
workflow.add_edge(START, 'parser_node')
workflow.add_edge('summarizer_node', END)

app = workflow.compile()
print(f"LangGraph 'DocumentProcessing' compiled.")


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

