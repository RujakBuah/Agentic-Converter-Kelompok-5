// Generated Mastra AI Framework (TypeScript)
// Source: aggregator.ttl
// System: Aggregator

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const aggregator_node = new Agent({
  name: "aggregator_node", 
  instructions: "Execute aggregator_node",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const aggregator_workflow = new Workflow({
  name: "Aggregator",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [aggregator_node],
} as any);

// --- VISUALIZATION HELPER ---
function printStructure(systemName: string, agents: any[]) {
    console.log("\n📊 MASTRA SYSTEM TOPOLOGY");
    console.log(`└── 📦 ${systemName}`);
    
    if(agents.length === 0) {
        console.log("    └── (No Agents Found)");
        return;
    }

    agents.forEach((agent, index) => {
        const isLast = index === agents.length - 1;
        const branch = isLast ? "└──" : "├──";
        console.log(`    ${branch} 🤖 ${agent.name}`);
    });
    console.log("\n");
}

// --- EXECUTION BLOCK ---
async function main() {
  console.log("🚀 Starting Real Mastra Workflow: Aggregator");
  
  const agentsList = [aggregator_node] as any[];
  printStructure("Aggregator", agentsList);

  console.log("✅ Workflow constructed successfully.");
}

main();
