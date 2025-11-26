import rdflib
from rdflib import Graph, Namespace, RDF
import re

AGENTO = Namespace("http://example.org/agento#")

def _clean_string(s):
    if not s: return ""
    s = str(s).strip().replace('"', '').replace('“', '').replace('”', '')
    return s

def _get_clean_id(g, subject, default_prefix="entity"):
    name = g.value(subject, AGENTO.name)
    if name: return _clean_string(name)
    
    node_name = g.value(subject, AGENTO.nodeName)
    if node_name: return _clean_string(node_name)
    
    uri_str = str(subject)
    if "#" in uri_str: return uri_str.split("#")[-1]
    if "/" in uri_str: return uri_str.split("/")[-1]
    return f"{default_prefix}_{str(subject)[-4:]}"

def _extract_name_from_justification(text):
    """
    Mencoba mengekstrak nama node dari teks deskripsi.
    Contoh input: 'Nama node selalu string ("planner_node").'
    Output: 'planner_node'
    """
    if not text: return None
    # Cari kata yang diapit tanda kutip atau kurung kutip
    matches = re.findall(r'["“]([a-zA-Z0-9_]+_node)["”]', str(text))
    if matches:
        return matches[0]
    return None

def extract_data(rdf_file_path):
    # --- 1. PRE-PROCESSING ---
    with open(rdf_file_path, "r", encoding="utf-8") as f:
        raw_content = f.read()

    header_patches = ""
    if "@prefix rdfs:" not in raw_content:
        header_patches += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    if "@prefix rdf:" not in raw_content:
        header_patches += "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
    
    g = Graph()
    try:
        g.parse(data=header_patches + raw_content, format="turtle")
    except Exception as e:
        print(f"  [RDF PARSE ERROR] {rdf_file_path}: {e}")
        return {"elements": []}

    filename = rdf_file_path.split("/")[-1].split("\\")[-1]
    # Nama sistem default dari nama file
    system_name = filename.replace(".ttl", "").replace("_", " ").title().replace(" ", "")
    
    unique_nodes = {}
    ordered_ids = []
    
    start_node_id = None
    end_node_id = None

    # --- STRATEGI 1: PENCARIAN STANDAR (Instance Based) ---
    subjects = list(g.subjects(RDF.type, AGENTO.Agent)) + list(g.subjects(RDF.type, AGENTO.Node))
    
    for subj in subjects:
        clean_id = _get_clean_id(g, subj, "node")
        vendor_class = str(g.value(subj, AGENTO.vendorClass) or "")
        
        # Override System Name
        if vendor_class == "name":
            system_name = clean_id.replace(" ", "")
            continue
            
        # Filter Schema/Metadata
        if any(k in vendor_class for k in ["Properti Graph", "StateGraph", "Node dalam Graph", "Node di dalam Graph", "workflow"]):
            continue
            
        # Deteksi Pointer
        if "set_entry_point" in vendor_class: start_node_id = clean_id
        if "finish_point" in vendor_class: end_node_id = clean_id
            
        instructions = g.value(subj, AGENTO.instructions)
        role = g.value(subj, AGENTO.role)
        func_label = g.value(subj, AGENTO.callableLabel)
        
        # Filter Node Sampah
        if clean_id.lower() in ["entry20point", "finish20point", "graph", "node", "workflow"]:
             if not instructions and not func_label: continue

        if clean_id not in unique_nodes:
            unique_nodes[clean_id] = {
                "id": clean_id,
                "type": "node",
                "desc": str(role) if role else "System Node",
                "logic": str(instructions or func_label) if (instructions or func_label) else f"Execute {clean_id}",
                "model": "gpt-4"
            }
            ordered_ids.append(clean_id)
        else:
            if instructions: unique_nodes[clean_id]["logic"] = str(instructions)

    # --- STRATEGI 2: FALLBACK (Schema/Justification Mining) ---
    # Jika Strategi 1 gagal menemukan node apapun, kita cari di properti justifikasi
    if not unique_nodes:
        props = list(g.subjects(RDF.type, AGENTO.DatatypeProperty))
        for prop in props:
            justification = g.value(prop, AGENTO.justification)
            if justification:
                # Coba extract nama node dari teks, misal: "planner_node" dari deskripsi
                hidden_name = _extract_name_from_justification(justification)
                if hidden_name and hidden_name not in unique_nodes:
                    unique_nodes[hidden_name] = {
                        "id": hidden_name,
                        "type": "node",
                        "desc": "Extracted from Schema",
                        "logic": f"Execute {hidden_name}",
                        "model": "gpt-4"
                    }
                    ordered_ids.append(hidden_name)
                    # Kita anggap node tunggal ini sebagai Start & End
                    if not start_node_id: start_node_id = hidden_name
                    if not end_node_id: end_node_id = hidden_name

    # --- FINAL CLEANUP ---
    if start_node_id == "aggregar_node" and "aggregator_node" in unique_nodes:
        start_node_id = "aggregator_node"
        if "aggregar_node" in unique_nodes:
            del unique_nodes["aggregar_node"]
            if "aggregar_node" in ordered_ids: ordered_ids.remove("aggregar_node")

    final_elements = [unique_nodes[uid] for uid in ordered_ids]

    return {
        "filename": filename,
        "system_name": system_name,
        "elements": final_elements,
        "explicit_start": start_node_id,
        "explicit_end": end_node_id
    }