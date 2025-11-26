# Generated LangGraph Framework
# Source: translation_service.ttl
# System: TranslationService

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def translator_node(state: GraphState):
    # Original Logic: Execute translator
    print(f"   [ACT] Node 'translator' is working...")
    return {"messages": ["Processed by translator_node"]}

def localizer_node(state: GraphState):
    # Original Logic: Execute localizer
    print(f"   [ACT] Node 'localizer' is working...")
    return {"messages": ["Processed by localizer_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('translator_node', translator_node)
workflow.add_node('localizer_node', localizer_node)
workflow.add_edge('translator_node', 'localizer_node')
workflow.add_edge(START, 'translator_node')
workflow.add_edge('localizer_node', END)

app = workflow.compile()
print(f"LangGraph 'TranslationService' compiled.")


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

