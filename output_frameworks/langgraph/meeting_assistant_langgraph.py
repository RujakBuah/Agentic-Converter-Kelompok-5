# Generated LangGraph Framework
# Source: meeting_assistant.ttl
# System: MeetingAssistant

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def scheduler_node(state: GraphState):
    # Original Logic: Execute scheduler
    print(f"   [ACT] Node 'scheduler' is working...")
    return {"messages": ["Processed by scheduler_node"]}

def note_taker_node(state: GraphState):
    # Original Logic: Execute note_taker
    print(f"   [ACT] Node 'note_taker' is working...")
    return {"messages": ["Processed by note_taker_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('scheduler_node', scheduler_node)
workflow.add_node('note_taker_node', note_taker_node)
workflow.add_edge('scheduler_node', 'note_taker_node')
workflow.add_edge(START, 'scheduler_node')
workflow.add_edge('note_taker_node', END)

app = workflow.compile()
print(f"LangGraph 'MeetingAssistant' compiled.")


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

