# Generated LangGraph Framework
# Source: content_creation.rdf
# System: ContentCreationPipeline

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---

def ideator_node(state: GraphState):
    # Original Logic: Generate content ideas
    print(f"   [ACT] Node 'ideator' is working...")
    new_msg = f"Processed by ideator"
    return {"messages": [new_msg]}

def writer_node(state: GraphState):
    # Original Logic: Write engaging content
    print(f"   [ACT] Node 'writer' is working...")
    new_msg = f"Processed by writer"
    return {"messages": [new_msg]}

def editor_node(state: GraphState):
    # Original Logic: Edit and refine content
    print(f"   [ACT] Node 'editor' is working...")
    new_msg = f"Processed by editor"
    return {"messages": [new_msg]}


# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

workflow.add_node('ideator', ideator_node)
workflow.add_edge('ideator', 'writer')
workflow.add_node('writer', writer_node)
workflow.add_edge('writer', 'editor')
workflow.add_node('editor', editor_node)
workflow.add_edge('editor', END)

workflow.add_edge(START, 'ideator')

app = workflow.compile()
print(f"LangGraph 'ContentCreationPipeline' compiled.")


if __name__ == "__main__":
    try:
        print("Build success. Visualizing Graph...")
        try:
            print(app.get_graph().draw_ascii())
        except Exception as e:
            print(f"[Info] Visualisasi Gagal: {e}")

        print("\n--- Starting Simulation ---")
        initial_state = {"messages": ["START_SIGNAL"]}
        result = app.invoke(initial_state)
        print("\n--- Final State Content ---")
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}")

