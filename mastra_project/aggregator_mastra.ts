// Generated Mastra AI Framework (TypeScript)
// Source: aggregator.rdf
// System: AgenticSystem

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const aggregator_node = new Agent({
  name: "aggregator_node",
  instructions: "lambda x: x",
  model: {
    provider: "OPEN_AI",
    name: "gpt-3.5-turbo",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const agenticsystem_workflow = new Workflow({
  name: "AgenticSystem",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [aggregator_node],
} as any);

// --- VISUALIZATION HELPER ---
function printStructure(systemName: string, agents: any[]) {
    console.log("\n📊 MASTRA SYSTEM TOPOLOGY");
    console.log(`└── 📦 ${systemName}`);
    console.log(`    │`);
    
    agents.forEach((agent, index) => {
        const isLast = index === agents.length - 1;
        const branch = isLast ? "└──" : "├──";
        const role = agent.role || "Agent Role";
        const model = agent.model?.name || "Unknown Model";
        
        console.log(`    ${branch} 🤖 ${agent.name}`);
        console.log(`    ${isLast ? "   " : "│  "}    ├── 📋 Role: ${role}`);
        console.log(`    ${isLast ? "   " : "│  "}    └── 🧠 Model: ${model}`);
    });
    console.log("\n");
}

// --- EXECUTION BLOCK ---
async function main() {
  console.log("🚀 Starting Real Mastra Workflow: AgenticSystem");
  
  // Ambil list agen untuk visualisasi
  const agentsList = [aggregator_node] as any[];
  
  // Panggil fungsi visualisasi
  printStructure("AgenticSystem", agentsList);

  console.log("✅ Workflow constructed successfully.");
  console.log("   Ready to connect to LLM Provider.");
}

main();
