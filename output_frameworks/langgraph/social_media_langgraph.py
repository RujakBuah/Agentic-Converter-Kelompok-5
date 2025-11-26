# Generated LangGraph Framework
# Source: social_media.ttl
# System: SocialMediaManager

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def content_planner_node(state: GraphState):
    # Original Logic: Execute content_planner
    print(f"   [ACT] Node 'content_planner' is working...")
    return {"messages": ["Processed by content_planner_node"]}

def post_creator_node(state: GraphState):
    # Original Logic: Execute post_creator
    print(f"   [ACT] Node 'post_creator' is working...")
    return {"messages": ["Processed by post_creator_node"]}

def engagement_monitor_node(state: GraphState):
    # Original Logic: Execute engagement_monitor
    print(f"   [ACT] Node 'engagement_monitor' is working...")
    return {"messages": ["Processed by engagement_monitor_node"]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('content_planner_node', content_planner_node)
workflow.add_node('post_creator_node', post_creator_node)
workflow.add_node('engagement_monitor_node', engagement_monitor_node)
workflow.add_edge('content_planner_node', 'post_creator_node')
workflow.add_edge('post_creator_node', 'engagement_monitor_node')
workflow.add_edge(START, 'content_planner_node')
workflow.add_edge('engagement_monitor_node', END)

app = workflow.compile()
print(f"LangGraph 'SocialMediaManager' compiled.")


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

