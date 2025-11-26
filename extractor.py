import rdflib
from rdflib import Graph, Namespace, RDF

AGENTO = Namespace("http://example.org/agento#")

def extract_data(rdf_file_path):
    # 1. PRE-PROCESSING (Inject Header)
    with open(rdf_file_path, "r", encoding="utf-8") as f:
        raw_content = f.read()

    header_patches = ""
    if "@prefix rdfs:" not in raw_content:
        header_patches += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    if "@prefix rdf:" not in raw_content:
        header_patches += "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
    
    patched_content = header_patches + raw_content

    g = Graph()
    try:
        g.parse(data=patched_content, format="turtle")
    except Exception as e:
        print(f"  [RDF PARSE ERROR] {e}")
        return {"elements": []}

    # 2. DATA EXTRACTION
    filename = rdf_file_path.split("/")[-1].split("\\")[-1]
    
    # Ambil nama sistem dari label Workflow atau System (jika ada)
    system_name = "AgenticSystem"
    roots = list(g.subjects(RDF.type, AGENTO.System)) + list(g.subjects(RDF.type, AGENTO.Workflow))
    if roots:
        lbl = g.value(roots[0], rdflib.RDFS.label)
        if lbl:
            system_name = str(lbl).replace(" ", "")

    elements = []

    # A. Cari AGENTS (Pola Mastra)
    # [cite_start]Referensi: code_review.rdf [cite: 582]
    agents = list(g.subjects(RDF.type, AGENTO.Agent))
    for agent in agents:
        role = g.value(agent, AGENTO.role)
        instructions = g.value(agent, AGENTO.instructions)
        # Ambil Model
        model_name = "gpt-4"
        cfg = g.value(agent, AGENTO.configuredBy)
        if cfg:
            mn = g.value(cfg, AGENTO.modelName)
            if mn: model_name = str(mn)
        
        elements.append({
            "id": str(agent).split("#")[-1],
            "type": "agent",
            "desc": str(role) if role else "Agent",
            "logic": str(instructions) if instructions else "Execute task",
            "model": str(model_name)
        })

    # B. Cari NODES (Pola LangGraph)
    # [cite_start]Referensi: analyzer.rdf [cite: 617]
    nodes = list(g.subjects(RDF.type, AGENTO.Node))
    for node in nodes:
        node_name = g.value(node, AGENTO.nodeName)
        func_label = g.value(node, AGENTO.callableLabel)
        
        elements.append({
            "id": str(node_name) if node_name else str(node).split("#")[-1],
            "type": "node",
            "desc": "Workflow Node", # Default desc untuk node
            "logic": str(func_label) if func_label else "lambda x: x",
            "model": "gpt-3.5-turbo" # Default model jika konversi Node -> Agent
        })

    return {
        "filename": filename,
        "system_name": system_name,
        "elements": elements
    }