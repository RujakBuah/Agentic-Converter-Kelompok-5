import os
import glob
from extractor import extract_data
from codegen import generate_mastra_code, generate_langgraph_code

# --- KONFIGURASI PATH BARU ---
BASE_INPUT_DIR = "input_rdfs"
SUB_DIRS = ["mastra", "langgraph"] # Dua folder kategori

OUTPUT_DIR = "output_frameworks"
MASTRA_PROJECT_DIR = "mastra_project"

def main():
    # Buat folder output
    langgraph_dir = os.path.join(OUTPUT_DIR, "langgraph")
    os.makedirs(langgraph_dir, exist_ok=True)
    os.makedirs(MASTRA_PROJECT_DIR, exist_ok=True)

    print(f"Starting Polyglot Conversion from '{BASE_INPUT_DIR}'...\n")
    
    stats = {"success": 0, "failed": 0, "skipped": 0}

    # Loop melalui setiap sub-folder (mastra dan langgraph)
    for sub in SUB_DIRS:
        current_input_path = os.path.join(BASE_INPUT_DIR, sub)
        
        # Cek apakah folder ada
        if not os.path.exists(current_input_path):
            print(f"[WARN] Folder not found: {current_input_path}. Skipping.")
            continue

        # Ambil semua file .ttl di folder tersebut
        ttl_files = glob.glob(os.path.join(current_input_path, "*.ttl"))
        print(f"--- Processing folder: /{sub} ({len(ttl_files)} files) ---")

        for input_file in ttl_files:
            try:
                data = extract_data(input_file)
                
                # Jika tidak ada elemen sama sekali, skip
                if not data["elements"]:
                    print(f"  [SKIP] {data['filename']} (No valid agents/nodes found)")
                    stats["skipped"] += 1
                    continue

                # 1. Generate MASTRA (TypeScript)
                # Kita generate untuk semua, tapi biasanya lebih relevan untuk folder 'mastra'
                mastra_code = generate_mastra_code(data)
                mastra_filename = data["filename"].replace(".ttl", "_mastra.ts") 
                mastra_path = os.path.join(MASTRA_PROJECT_DIR, mastra_filename)
                
                with open(mastra_path, "w", encoding="utf-8") as f:
                    f.write(mastra_code)
                
                # 2. Generate LANGGRAPH (Python)
                lg_code = generate_langgraph_code(data)
                lg_filename = data["filename"].replace(".ttl", "_langgraph.py")
                lg_path = os.path.join(langgraph_dir, lg_filename)
                
                with open(lg_path, "w", encoding="utf-8") as f:
                    f.write(lg_code)

                print(f"  [OK] {data['filename']} -> TS & PY generated.")
                stats["success"] += 1

            except Exception as e:
                print(f"  [ERROR] {input_file}: {e}")
                stats["failed"] += 1
        print("") # Newline antar folder

    print("="*30)
    print("CONVERSION SUMMARY")
    print("="*30)
    print(f"Total Processed        : {stats['success'] + stats['failed'] + stats['skipped']}")
    print(f"Success                : {stats['success']}")
    print(f"Mastra Location (TS)   : ./{MASTRA_PROJECT_DIR}/")
    print(f"LangGraph Location (PY): ./{langgraph_dir}/")
    print("="*30)

if __name__ == "__main__":
    main()