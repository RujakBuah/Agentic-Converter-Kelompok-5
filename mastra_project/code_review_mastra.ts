// Generated Mastra AI Framework (TypeScript)
// Source: code_review.rdf
// System: CodeReviewSystem

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const reviewer = new Agent({
  name: "reviewer",
  instructions: "Review code for quality and best practices",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const tester = new Agent({
  name: "tester",
  instructions: "Generate and run tests",
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
  console.log("🚀 Starting Real Mastra Workflow: CodeReviewSystem");
  
  // Ambil list agen untuk visualisasi
  const agentsList = [reviewer, tester] as any[];
  
  // Panggil fungsi visualisasi
  printStructure("CodeReviewSystem", agentsList);

  console.log("✅ Workflow constructed successfully.");
  console.log("   Ready to connect to LLM Provider.");
}

main();
