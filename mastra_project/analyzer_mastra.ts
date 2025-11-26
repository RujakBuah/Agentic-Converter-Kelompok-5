// Generated Mastra AI Framework (TypeScript)
// Source: analyzer.ttl
// System: Analyzer

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const analyzer_node = new Agent({
  name: "analyzer_node", 
  instructions: "Execute analyzer_node",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const analyze_node = new Agent({
  name: "analyze_node", 
  instructions: "Execute analyze_node",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const analyzer_workflow = new Workflow({
  name: "Analyzer",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [analyzer_node, analyze_node],
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
  console.log("🚀 Starting Real Mastra Workflow: Analyzer");
  
  const agentsList = [analyzer_node, analyze_node] as any[];
  printStructure("Analyzer", agentsList);

  console.log("✅ Workflow constructed successfully.");
}

main();
