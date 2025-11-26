// Generated Mastra AI (TypeScript)
// Source: customer_support.rdf
// Reference: CustomerSupportSystem

import { Agent, Workflow } from '@mastra/core';

// --- AGENT DEFINITIONS ---

const supportagent = new Agent({
  name: "supportAgent",
  role: "Support Agent",
  instructions: "Handle customer inquiries",
  model: {
    provider: "openai", // Asumsi default
    name: "gpt-4",
    toolChoice: "auto"
  }
});

const escalationagent = new Agent({
  name: "escalationAgent",
  role: "Escalation Specialist",
  instructions: "Handle complex issues",
  model: {
    provider: "openai", // Asumsi default
    name: "gpt-4",
    toolChoice: "auto"
  }
});


// --- WORKFLOW DEFINITION ---
const systemWorkflow = new Workflow({
  name: "CustomerSupportSystem",
  triggerSchema: {}, 
  agents: [supportagent, escalationagent]
});

// --- EXECUTION (Simulasi Run) ---
async function main() {
  console.log("Starting Mastra Workflow: CustomerSupportSystem");
  
  // Contoh menjalankan salah satu agen (karena Mastra butuh trigger spesifik)
  // Di sini kita hanya men-log strukturnya agar valid
  console.log("Agents loaded:", ['supportagent', 'escalationagent']);
  
  // Real execution would require an LLM API Key
  console.log("System ready.");
}

main();
