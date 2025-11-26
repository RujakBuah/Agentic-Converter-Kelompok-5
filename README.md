# Agentic AI Framework Converter (Group 5)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![TypeScript](https://img.shields.io/badge/TypeScript-5.0%2B-blue) ![Mastra](https://img.shields.io/badge/Framework-Mastra_AI-orange) ![LangGraph](https://img.shields.io/badge/Framework-LangGraph-green)

An automated pipeline designed to transform semantic Knowledge Graphs (RDF) into executable Agentic AI frameworks. This tool supports **polyglot generation**, converting a single RDF source pattern into both **LangGraph (Python)** and **Mastra AI (TypeScript)** implementations.

Developed for the **Agentic AI Framework** course assignment (Week 3), based on the semantic foundations outlined in the *K-CAP 2025* paper.

## Key Features

* **Dual-Framework Generation:** Automatically converts RDF definitions into:
    * **LangGraph:** Graph-based stateful orchestration (Python).
    * **Mastra AI:** Agent-centric orchestration (TypeScript).
* **Robust RDF Parsing:** Handles RDF files with or without standard header prefixes via a resilient extractor.
* **Runnable Output:** Generated code includes execution blocks with state simulation and ASCII visualizations.
* **Synthetic Data Generator:** Includes a tool to generate synthetic RDF patterns to test scalability (supports 25+ patterns).

## Project Structure

```text
Agentic-Converter-Kelompok-5/
├── input_rdfs/              # Source Knowledge Graphs (.rdf files)
├── output_frameworks/       # Generated LangGraph code
│   └── langgraph/           # Python files (.py)
├── mastra_project/          # Generated Mastra AI project & code
│   ├── node_modules/        # Node.js dependencies (ignored in git)
│   ├── package.json         # Mastra configuration
│   └── ..._mastra.ts        # TypeScript files (.ts)
├── codegen.py               # Template engine (Python & TypeScript generation logic)
├── extractor.py             # RDF parsing logic
├── main.py                  # Main orchestration pipeline
├── synthetic_data.py        # Script to generate dummy RDF patterns
└── requirements.txt         # Python dependencies
```

## Installation & Setup

This project requires **Python** and **Node.js**. Follow these steps to set up the environment.

### 1. Clone the Repository
```bash
git clone https://github.com/RujakBuah/Agentic-Converter-Kelompok-5.git
cd Agentic-Converter-Kelompok-5
git checkout week3
```

### 2. Python Setup (for Pipeline & LangGraph)
It is recommended to use a virtual environment.

**Windows:**
```powershell
# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Node.js Setup (for Mastra AI)
Navigate to the Mastra project folder and install dependencies.

```bash
cd mastra_project
npm install
cd ..
```

---

## How to Run

### Step 1: Generate Frameworks
Run the main pipeline to read all RDF files from `input_rdfs/` and generate the corresponding code.

```bash
python main.py
```
*Output:* You will see logs indicating successful conversion for both Mastra and LangGraph formats.

### Step 2: Run Generated LangGraph Code (Python)
The generated Python files are located in `output_frameworks/langgraph/`.

```bash
# Example: Running the Customer Support system
python output_frameworks/langgraph/customer_support_langgraph.py
```
*Expected Output:* ASCII graph visualization and state execution logs.

### Step 3: Run Generated Mastra Code (TypeScript)
The generated TypeScript files are located in `mastra_project/`. Use `npx tsx` to execute them directly.

```bash
cd mastra_project

# Example: Running the Customer Support system
npx tsx customer_support_mastra.ts
```
*Expected Output:* System topology visualization and agent role verification.

## 👥 Authors (Group 5)
* Sultan Rizqinta Sinuraya (23/516307/PA/22087)
* Muhammad Farhan Hanim (23/518027/PA/22230)
* Muhammad Fariz (23/518174/PA/22237)

---
*Note: The `node_modules` folder is excluded from this repository to ensure a lightweight clone. You must run `npm install` inside `mastra_project` before running any TypeScript files.*
