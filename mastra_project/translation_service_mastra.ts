// Generated Mastra AI Framework (TypeScript)
// Source: translation_service.ttl
// System: TranslationService

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const translator = new Agent({
  name: "translator", 
  instructions: "Execute translator",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const localizer = new Agent({
  name: "localizer", 
  instructions: "Execute localizer",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const translationservice_workflow = new Workflow({
  name: "TranslationService",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [translator, localizer],
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
  console.log("🚀 Starting Real Mastra Workflow: TranslationService");
  
  const agentsList = [translator, localizer] as any[];
  printStructure("TranslationService", agentsList);

  console.log("✅ Workflow constructed successfully.");
}

main();
