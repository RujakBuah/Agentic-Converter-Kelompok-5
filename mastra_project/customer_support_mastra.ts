// Generated Mastra AI Framework (TypeScript)
// Source: customer_support.rdf
// System: CustomerSupportSystem

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const supportagent = new Agent({
  name: "supportAgent",
  instructions: "Handle customer inquiries",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const escalationagent = new Agent({
  name: "escalationAgent",
  instructions: "Handle complex issues",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const customersupportsystem_workflow = new Workflow({
  name: "CustomerSupportSystem",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [supportagent, escalationagent],
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
  console.log("🚀 Starting Real Mastra Workflow: CustomerSupportSystem");
  
  // Ambil list agen untuk visualisasi
  const agentsList = [supportagent, escalationagent] as any[];
  
  // Panggil fungsi visualisasi
  printStructure("CustomerSupportSystem", agentsList);

  console.log("✅ Workflow constructed successfully.");
  console.log("   Ready to connect to LLM Provider.");
}

main();
