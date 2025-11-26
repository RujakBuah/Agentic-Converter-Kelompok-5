// Generated Mastra AI Framework (TypeScript)
// Source: code_review.ttl
// System: CodeReviewSystem

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const reviewer = new Agent({
  name: "reviewer", 
  instructions: "Execute reviewer",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const tester = new Agent({
  name: "tester", 
  instructions: "Execute tester",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const codereviewsystem_workflow = new Workflow({
  name: "CodeReviewSystem",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [reviewer, tester],
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
  console.log("🚀 Starting Real Mastra Workflow: CodeReviewSystem");
  
  const agentsList = [reviewer, tester] as any[];
  printStructure("CodeReviewSystem", agentsList);

  console.log("✅ Workflow constructed successfully.");
}

main();
