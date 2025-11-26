// Generated Mastra AI Framework (TypeScript)
// Source: content_creation.rdf
// System: ContentCreationPipeline

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const ideator = new Agent({
  name: "ideator",
  instructions: "Generate content ideas",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const writer = new Agent({
  name: "writer",
  instructions: "Write engaging content",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const editor = new Agent({
  name: "editor",
  instructions: "Edit and refine content",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const contentcreationpipeline_workflow = new Workflow({
  name: "ContentCreationPipeline",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [ideator, writer, editor],
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
  console.log("🚀 Starting Real Mastra Workflow: ContentCreationPipeline");
  
  // Ambil list agen untuk visualisasi
  const agentsList = [ideator, writer, editor] as any[];
  
  // Panggil fungsi visualisasi
  printStructure("ContentCreationPipeline", agentsList);

  console.log("✅ Workflow constructed successfully.");
  console.log("   Ready to connect to LLM Provider.");
}

main();
