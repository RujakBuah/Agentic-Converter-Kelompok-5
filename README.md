# Agentic Converter — Kelompok 5 (Week 3)

## Overview
This project implements an automated pipeline that converts Agentic AI Pattern Knowledge Graphs (KGs) into executable code for two Agentic AI frameworks: LangGraph and MastraAI.

## Motivation
Agentic AI workflows consist of reusable patterns involving agents, tasks, tools, and transitions. Group 3 provided these patterns as Knowledge Graphs based on the Agentic AI Ontology. This project automates the conversion of those semantic representations into framework-specific runnable code.

## Project Architecture
```
agentic-converter-kelompok-5/
- pipeline/
  - ingest.py
  - extractor.py
  - codegen.py
  - mappings.yaml
  - templates/
    - langgraph/graph.j2.json
    - mastra/assistant.j2.ts
- examples/kg_sample.ttl
- reports/checklist_week2.md
- requirements.txt
- package.json
```

## Pipeline Modules
1. Ingestion Module
2. Extraction Module
3. Mapping Module
4. Code Generation Module

## Testing
The script pipeline/tests_smoke.py performs smoke tests validating generated output and produces reports/checklist_week(n).md

## Week 3 Progress Summary
- Pipeline fully operational for sample patterns
- Templates validated for LangGraph and MastraAI
- Extraction correctness validated on sample KG

Ongoing:
- Expanding SPARQL rules and scaling to 25 patterns
- Extending mapping and semantic validation

## How to Run
```
pip install -r requirements.txt
python pipeline/codegen.py examples/kg_sample.ttl examples/generated
python pipeline/tests_smoke.py
```

## Contributors
Kelompok 5 - Semantic Web 2025
- Sultan Rizqinta Sinuraya
- Muhammad Farhan Hanim
- Muhammad Fariz
