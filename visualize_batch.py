import os
import sys
import glob
import importlib.util

# --- KONFIGURASI ---
# Lokasi file python hasil generate
INPUT_DIR = os.path.join("output_frameworks", "langgraph")
# Lokasi output gambar
OUTPUT_DIR = "graph_visualizations"

def main():
    # 1. Buat folder output khusus gambar
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"[INFO] Created visualization directory: {OUTPUT_DIR}")

    # 2. Tambahkan folder input ke sys.path agar modul bisa di-import dengan benar
    abs_input_dir = os.path.abspath(INPUT_DIR)
    sys.path.append(abs_input_dir)

    # 3. Cari semua file *_langgraph.py
    py_files = glob.glob(os.path.join(INPUT_DIR, "*_langgraph.py"))
    
    if not py_files:
        print(f"[WARN] No Python files found in {INPUT_DIR}.")
        return

    print(f"[INFO] Found {len(py_files)} frameworks. Starting batch visualization...\n")

    success_count = 0
    fail_count = 0

    for file_path in py_files:
        filename = os.path.basename(file_path)
        module_name = filename.replace(".py", "")
        
        print(f"[EXEC] Processing: {filename}...")
        
        try:
            # --- TEKNIK DYNAMIC IMPORT ---
            # Kita me-load file python tersebut sebagai module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            
            # Eksekusi module (sama seperti 'import ...')
            spec.loader.exec_module(module)
            
            # --- GENERASI GRAPH ---
            # Kita cari variabel 'app' (compiled workflow) di dalam module
            if hasattr(module, 'app'):
                # Dapatkan object graph
                graph = module.app.get_graph()
                
                # Generate PNG (Membutuhkan koneksi internet untuk API Mermaid Ink default)
                try:
                    png_data = graph.draw_mermaid_png()
                    
                    # Simpan ke file
                    output_filename = filename.replace(".py", ".png")
                    output_path = os.path.join(OUTPUT_DIR, output_filename)
                    
                    with open(output_path, "wb") as f:
                        f.write(png_data)
                        
                    print(f"   [OK] Saved image to: {output_path}")
                    success_count += 1
                    
                except Exception as img_err:
                    print(f"   [ERR] Failed to draw PNG: {img_err}")
                    print("         (Check internet connection or graph structure)")
                    fail_count += 1
            else:
                print(f"   [SKIP] Module '{module_name}' does not have 'app' object.")
                fail_count += 1

        except Exception as e:
            print(f"   [ERR] Failed to import/execute module: {e}")
            fail_count += 1

    print("\n" + "="*30)
    print("BATCH VISUALIZATION SUMMARY")
    print(f"Total Files : {len(py_files)}")
    print(f"Success     : {success_count}")
    print(f"Failed      : {fail_count}")
    print(f"Location    : ./{OUTPUT_DIR}/")
    print("="*30)

if __name__ == "__main__":
    main()