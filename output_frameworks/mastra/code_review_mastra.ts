// Generated Mastra AI (TypeScript)
// Source: code_review.rdf
// Reference: CodeReviewSystem

import { Agent, Workflow } from '@mastra/core';

// --- AGENT DEFINITIONS ---

const reviewer = new Agent({
  name: "reviewer",
  role: "Code Reviewer",
  instructions: "Review code for quality and best practices",
  model: {
    provider: "openai", // Asumsi default
    name: "gpt-4",
    toolChoice: "auto"
  }
});

const tester = new Agent({
  name: "tester",
  role: "Test Engineer",
  instructions: "Generate and run tests",
  model: {
    provider: "openai", // Asumsi default
    name: "gpt-4",
    toolChoice: "auto"
  }
});


// --- WORKFLOW DEFINITION ---
const systemWorkflow = new Workflow({
  name: "CodeReviewSystem",
  triggerSchema: {}, 
  agents: [reviewer, tester]
});

// --- EXECUTION (Simulasi Run) ---
async function main() {
  console.log("Starting Mastra Workflow: CodeReviewSystem");
  
  // Contoh menjalankan salah satu agen (karena Mastra butuh trigger spesifik)
  // Di sini kita hanya men-log strukturnya agar valid
  console.log("Agents loaded:", ['reviewer', 'tester']);
  
  // Real execution would require an LLM API Key
  console.log("System ready.");
}

main();
