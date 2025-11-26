// Generated Mastra AI (TypeScript)
// Source: classifier.rdf
// Reference: AgenticSystem

import { Agent, Workflow } from '@mastra/core';

// --- AGENT DEFINITIONS ---

const classifier_node = new Agent({
  name: "classifier_node",
  role: "Workflow Node",
  instructions: "lambda x: x",
  model: {
    provider: "openai", // Asumsi default
    name: "gpt-3.5-turbo",
    toolChoice: "auto"
  }
});


// --- WORKFLOW DEFINITION ---
const systemWorkflow = new Workflow({
  name: "AgenticSystem",
  triggerSchema: {}, 
  agents: [classifier_node]
});

// --- EXECUTION (Simulasi Run) ---
async function main() {
  console.log("Starting Mastra Workflow: AgenticSystem");
  
  // Contoh menjalankan salah satu agen (karena Mastra butuh trigger spesifik)
  // Di sini kita hanya men-log strukturnya agar valid
  console.log("Agents loaded:", ['classifier_node']);
  
  // Real execution would require an LLM API Key
  console.log("System ready.");
}

main();
