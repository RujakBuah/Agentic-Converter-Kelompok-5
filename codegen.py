def generate_mastra_code(data):
    # Template TypeScript (Real Mastra) - Dengan Visualisasi ASCII
    
    agent_defs = ""
    agent_names = []
    
    for el in data["elements"]:
        safe_id = el['id'].replace(" ", "_").lower().replace("-", "_")
        agent_names.append(safe_id)
        clean_instr = el['logic'].replace("\n", " ").replace('"', "'")
        
        # Tetap menggunakan 'as any' agar aman dari error strict type
        agent_defs += f"""
const {safe_id} = new Agent({{
  name: "{el['id']}",
  instructions: "{clean_instr}",
  model: {{
    provider: "OPEN_AI",
    name: "{el['model']}",
    toolChoice: "auto",
  }} as any,
}});
"""

    agent_list_str = ", ".join(agent_names)

    return f"""// Generated Mastra AI Framework (TypeScript)
// Source: {data['filename']}
// System: {data['system_name']}

import {{ Agent, Workflow }} from '@mastra/core';
import {{ z }} from 'zod';

// --- AGENT DEFINITIONS ---
{agent_defs}

// --- WORKFLOW DEFINITION ---
const {data['system_name'].lower()}_workflow = new Workflow({{
  name: "{data['system_name']}",
  triggerSchema: z.object({{
    task: z.string(),
  }}),
  agents: [{agent_list_str}],
}} as any);

// --- VISUALIZATION HELPER ---
function printStructure(systemName: string, agents: any[]) {{
    console.log("\\n📊 MASTRA SYSTEM TOPOLOGY");
    console.log(`└── 📦 ${{systemName}}`);
    console.log(`    │`);
    
    agents.forEach((agent, index) => {{
        const isLast = index === agents.length - 1;
        const branch = isLast ? "└──" : "├──";
        const role = agent.role || "Agent Role";
        const model = agent.model?.name || "Unknown Model";
        
        console.log(`    ${{branch}} 🤖 ${{agent.name}}`);
        console.log(`    ${{isLast ? "   " : "│  "}}    ├── 📋 Role: ${{role}}`);
        console.log(`    ${{isLast ? "   " : "│  "}}    └── 🧠 Model: ${{model}}`);
    }});
    console.log("\\n");
}}

// --- EXECUTION BLOCK ---
async function main() {{
  console.log("🚀 Starting Real Mastra Workflow: {data['system_name']}");
  
  // Ambil list agen untuk visualisasi
  const agentsList = [{agent_list_str}] as any[];
  
  // Panggil fungsi visualisasi
  printStructure("{data['system_name']}", agentsList);

  console.log("✅ Workflow constructed successfully.");
  console.log("   Ready to connect to LLM Provider.");
}}

main();
"""

def generate_langgraph_code(data):
    # ... (Bagian LangGraph biarkan sama seperti sebelumnya) ...
    # Pastikan copy-paste bagian LangGraph dari kode sebelumnya jika tertimpa
    node_funcs = ""
    graph_add = ""
    elements = data["elements"]
    
    for i, el in enumerate(elements):
        safe_id = el['id'].replace(" ", "_").lower().replace("-", "_")
        logic_comment = f"# Original Logic: {el['logic']}"
        node_funcs += f"""
def {safe_id}_node(state: GraphState):
    {logic_comment}
    print(f"   [ACT] Node '{safe_id}' is working...")
    new_msg = f"Processed by {safe_id}"
    return {{"messages": [new_msg]}}
"""
        graph_add += f"workflow.add_node('{safe_id}', {safe_id}_node)\n"
        if i < len(elements) - 1:
            next_id = elements[i+1]['id'].replace(" ", "_").lower().replace("-", "_")
            graph_add += f"workflow.add_edge('{safe_id}', '{next_id}')\n"
        else:
            graph_add += f"workflow.add_edge('{safe_id}', END)\n"

    if elements:
        first_id = elements[0]['id'].replace(" ", "_").lower().replace("-", "_")
        start_edge = f"workflow.add_edge(START, '{first_id}')"
    else:
        start_edge = "# No elements to connect"

    execution_block = f"""
if __name__ == "__main__":
    try:
        print("Build success. Visualizing Graph...")
        try:
            print(app.get_graph().draw_ascii())
        except Exception as e:
            print(f"[Info] Visualisasi Gagal: {{e}}")

        print("\\n--- Starting Simulation ---")
        initial_state = {{"messages": ["START_SIGNAL"]}}
        result = app.invoke(initial_state)
        print("\\n--- Final State Content ---")
        print(result)
    except Exception as e:
        print(f"Runtime Error: {{e}}")
"""

    return f"""# Generated LangGraph Framework
# Source: {data['filename']}
# System: {data['system_name']}

from langgraph.graph import StateGraph, START, END
from typing import Dict, List, Annotated
import operator

class GraphState(Dict):
    messages: Annotated[List[str], operator.add]

# --- NODE FUNCTIONS ---
{node_funcs}

# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(GraphState)

{graph_add}
{start_edge}

app = workflow.compile()
print(f"LangGraph '{data['system_name']}' compiled.")

{execution_block}
"""