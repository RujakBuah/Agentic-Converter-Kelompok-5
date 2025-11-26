// Generated Mastra AI Framework (TypeScript)
// Source: hr_assistant.ttl
// System: HRAssistant

import { Agent, Workflow } from '@mastra/core';
import { z } from 'zod';

// --- AGENT DEFINITIONS ---

const recruiter = new Agent({
  name: "recruiter", 
  instructions: "Execute recruiter",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});

const onboarding_guide = new Agent({
  name: "onboarding_guide", 
  instructions: "Execute onboarding_guide",
  model: {
    provider: "OPEN_AI",
    name: "gpt-4",
    toolChoice: "auto",
  } as any,
});


// --- WORKFLOW DEFINITION ---
const hrassistant_workflow = new Workflow({
  name: "HRAssistant",
  triggerSchema: z.object({
    task: z.string(),
  }),
  agents: [recruiter, onboarding_guide],
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
  console.log("🚀 Starting Real Mastra Workflow: HRAssistant");
  
  const agentsList = [recruiter, onboarding_guide] as any[];
  printStructure("HRAssistant", agentsList);

  console.log("✅ Workflow constructed successfully.");
}

main();
