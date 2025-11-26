# Agentic AI Framework Converter (Group 5)

![Python](https://img.shields.io/badge/Python-3.12%2B-blue) ![TypeScript](https://img.shields.io/badge/TypeScript-5.0%2B-blue) ![Mastra](https://img.shields.io/badge/Framework-Mastra_AI-orange) ![LangGraph](https://img.shields.io/badge/Framework-LangGraph-green)

An automated pipeline designed to transform semantic Knowledge Graphs (RDF/Turtle) into executable Agentic AI frameworks. This tool supports **polyglot generation**, converting semantic source patterns into both **LangGraph (Python)** and **Mastra AI (TypeScript)** implementations.

Developed for the **Agentic AI Framework** course assignment, based on the semantic foundations outlined in the *K-CAP 2025* paper.

## Key Features

* **Polyglot Input Handling:** Smartly processes two types of input definitions:
    * **Type 1 (Structural):** Low-level graph definitions (Nodes, Edges, Start/End) optimized for LangGraph.
    * **Type 2 (Agentic):** High-level agent roles and instructions optimized for Mastra AI.
* **Dual-Framework Generation:** Automatically converts `.ttl` files into:
    * **LangGraph:** Graph-based stateful orchestration (Python).
    * **Mastra AI:** Agent-centric orchestration (TypeScript).
* **Batch Execution & Logging:** Includes an automated runner (`run_experiments.py`) to execute all generated frameworks and log results.
* **Advanced Visualization:** Generates **Mermaid.js** diagrams and automatically saves them as PNG images via a batch visualizer.
* **Robust Extraction:** Features "Heuristic Extraction" to recover node definitions even from abstract schema files.

## Project Structure

```text
Agentic-Converter-Kelompok-5/
├── input_rdfs/              # Source Knowledge Graphs (.ttl files)
│   ├── langgraph/           # Type 1: Structural definitions (e.g., aggregator, classifier)
│   └── mastra/              # Type 2: Agentic definitions (e.g., code_review, customer_support)
├── output_frameworks/
│   └── langgraph/           # Generated LangGraph Python code (.py)
├── mastra_project/          # Generated Mastra AI project & code
│   ├── node_modules/        # Node.js dependencies
│   ├── package.json         # Mastra configuration
│   └── ..._mastra.ts        # Generated TypeScript files
├── execution_results/       # [NEW] Logs & ASCII outputs from batch execution
├── graph_visualizations/    # [NEW] Generated Mermaid Graph PNGs
├── codegen.py               # Template engine (Code generation logic)
├── extractor.py             # RDF parsing & heuristic logic
├── main.py                  # Main orchestration pipeline (Polyglot Converter)
├── run_experiments.py       # Batch runner for Python frameworks
├── visualize_batch.py       # Batch PNG generator for Graphs
└── requirements.txt         # Python dependencies
```

## Installation & Setup

This project requires **Python**. Follow these steps to set up the environment.

### 1. Clone the Repository
```bash
git clone [https://github.com/RujakBuah/Agentic-Converter-Kelompok-5.git](https://github.com/RujakBuah/Agentic-Converter-Kelompok-5.git)
cd Agentic-Converter-Kelompok-5
```

### 2. Python Setup (for Pipeline & LangGraph)
It is recommended to use a virtual environment.

**Windows:**
```powershell
# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate

# Install dependencies (ensure grandalf and other libs are installed)
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Node.js Setup (Optional, for Mastra AI)
Navigate to the Mastra project folder and install dependencies.

```bash
cd mastra_project
npm install
cd ..
```

---

## How to Run

### Step 1: Generate Frameworks (Polyglot Conversion)
Run the main pipeline. This will scan both `input_rdfs/langgraph` and `input_rdfs/mastra` folders and generate the corresponding code.

```bash
python main.py
```
*Output:* You will see logs indicating successful conversion (e.g., `[OK] aggregator.ttl -> TS & PY generated`).

### Step 2: Batch Execute Frameworks (Python)
Instead of running files manually, use the experiment runner to execute all generated LangGraph frameworks at once. This script handles encoding safety and captures logs.

```bash
python run_experiments.py
```
*Output:* Check the **`execution_results/`** folder. You will find text files containing execution logs and simulation outputs for each framework.

### Step 3: Generate Visualizations (Mermaid PNG)
To generate visual representations of the workflows (Shapes & Lines), run the visualization script. *Requires active internet connection to render Mermaid diagrams.*

```bash
python visualize_batch.py
```
*Output:* Check the **`graph_visualizations/`** folder. You will find `.png` images representing the graph topology for each system.

### Step 4: Run Generated Mastra Code (TypeScript, Optional)
The generated TypeScript files are located in `mastra_project/`. Use `npx tsx` to execute them directly.

```bash
cd mastra_project

# Example: Running the Customer Support system
npx tsx customer_support_mastra.ts
```
*Expected Output:* System topology visualization and agent role verification in the console.

## Authors (Group 5)
* Sultan Rizqinta Sinuraya (23/516307/PA/22087)
* Muhammad Farhan Hanim (23/518027/PA/22230)
* Muhammad Fariz (23/518174/PA/22237)

---
*Note: The `node_modules` folder is excluded from this repository to ensure a lightweight clone.*