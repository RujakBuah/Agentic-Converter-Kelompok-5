# Generated LangGraph Framework
# Source: customer_support.ttl
# System: CustomerSupportSystem

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def support_agent_node(state: GraphState):
    # Original Logic: Execute support_agent
    print(f"   [ACT] Node 'support_agent' is working...")
    return {"messages": ["Processed by support_agent_node"]}

def escalation_agent_node(state: GraphState):
    # Original Logic: Execute escalation_agent
    print(f"   [ACT] Node 'escalation_agent' is working...")
    return {"messages": ["Processed by escalation_agent_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('support_agent_node', support_agent_node)
workflow.add_node('escalation_agent_node', escalation_agent_node)
workflow.add_edge('support_agent_node', 'escalation_agent_node')
workflow.add_edge(START, 'support_agent_node')
workflow.add_edge('escalation_agent_node', END)

app = workflow.compile()
print(f"LangGraph 'CustomerSupportSystem' compiled.")


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

