import os
import glob
from extractor import extract_data
from codegen import generate_mastra_code, generate_langgraph_code

INPUT_DIR = "input_rdfs"
OUTPUT_DIR = "output_frameworks"
MASTRA_PROJECT_DIR = "mastra_project" # Folder tempat Anda install npm tadi

def main():
    # Folder output Python (LangGraph)
    langgraph_dir = os.path.join(OUTPUT_DIR, "langgraph")
    os.makedirs(langgraph_dir, exist_ok=True)
    
    # Folder output TypeScript (Mastra)
    # Kita simpan langsung ke folder project node.js agar bisa di-run
    os.makedirs(MASTRA_PROJECT_DIR, exist_ok=True)

    rdf_files = glob.glob(os.path.join(INPUT_DIR, "*.rdf"))
    print(f"Found {len(rdf_files)} RDF files. Starting Polyglot Conversion...\n")
    
    stats = {"success": 0, "failed": 0}

    for rdf_file in rdf_files:
        try:
            print(f"Processing: {rdf_file}...")
            data = extract_data(rdf_file)
            
            if not data["elements"]:
                print(f"  [WARN] No agents/nodes found in {rdf_file}. Skipping.")
                stats["failed"] += 1
                continue

            # 1. Generate MASTRA (TypeScript) -> Save ke mastra_project/
            mastra_code = generate_mastra_code(data)
            mastra_filename = data["filename"].replace(".rdf", "_mastra.ts") # .ts extension
            mastra_path = os.path.join(MASTRA_PROJECT_DIR, mastra_filename)
            
            with open(mastra_path, "w", encoding="utf-8") as f:
                f.write(mastra_code)
            
            # 2. Generate LANGGRAPH (Python) -> Save ke output_frameworks/langgraph/
            lg_code = generate_langgraph_code(data)
            lg_filename = data["filename"].replace(".rdf", "_langgraph.py")
            lg_path = os.path.join(langgraph_dir, lg_filename)
            
            with open(lg_path, "w", encoding="utf-8") as f:
                f.write(lg_code)

            print(f"  [SUCCESS] Generated:")
            print(f"     - TS: {mastra_path}")
            print(f"     - PY: {lg_path}")
            stats["success"] += 1

        except Exception as e:
            print(f"  [ERROR] Failed to process {rdf_file}: {e}")
            stats["failed"] += 1

    print("\n" + "="*30)
    print("POLYGLOT CONVERSION SUMMARY")
    print("="*30)
    print(f"Total Inputs           : {len(rdf_files)}")
    print(f"Total Frameworks Built : {stats['success'] * 2}")
    print(f"Mastra Location (TS)   : ./{MASTRA_PROJECT_DIR}/")
    print(f"LangGraph Location (PY): ./{langgraph_dir}/")
    print("="*30)

if __name__ == "__main__":
    main()