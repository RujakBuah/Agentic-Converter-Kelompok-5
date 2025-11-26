# Generated LangGraph Framework
# Source: hr_assistant.ttl
# System: HRAssistant

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def recruiter_node(state: GraphState):
    # Original Logic: Execute recruiter
    print(f"   [ACT] Node 'recruiter' is working...")
    return {"messages": ["Processed by recruiter_node"]}

def onboarding_guide_node(state: GraphState):
    # Original Logic: Execute onboarding_guide
    print(f"   [ACT] Node 'onboarding_guide' is working...")
    return {"messages": ["Processed by onboarding_guide_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('recruiter_node', recruiter_node)
workflow.add_node('onboarding_guide_node', onboarding_guide_node)
workflow.add_edge('recruiter_node', 'onboarding_guide_node')
workflow.add_edge(START, 'recruiter_node')
workflow.add_edge('onboarding_guide_node', END)

app = workflow.compile()
print(f"LangGraph 'HRAssistant' compiled.")


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

