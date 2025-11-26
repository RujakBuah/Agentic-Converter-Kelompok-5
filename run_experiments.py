import os
import glob
import subprocess
import sys

# --- KONFIGURASI ---
LANGGRAPH_DIR = os.path.join("output_frameworks", "langgraph")
RESULTS_DIR = "execution_results"

def main():
    # Mengatur output agar mendukung UTF-8 (Opsional)
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except:
            pass

    # Cek lokasi python yang sedang digunakan (untuk debugging)
    print(f"[INFO] Running with Python interpreter: {sys.executable}")

    # 1. Buat folder hasil jika belum ada
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        print(f"[INFO] Created results directory: {RESULTS_DIR}")

    # 2. Cari semua file generated python
    py_files = glob.glob(os.path.join(LANGGRAPH_DIR, "*_langgraph.py"))
    
    if not py_files:
        print(f"[WARN] No Python files found in {LANGGRAPH_DIR}. Run main.py first.")
        return

    print(f"[INFO] Found {len(py_files)} frameworks to execute.\n")

    # 3. Loop dan Eksekusi
    for py_file in py_files:
        filename = os.path.basename(py_file)
        print(f"[EXEC] Executing: {filename}...")
        
        try:
            # PERBAIKAN: Gunakan sys.executable agar subprocess memakai python venv yang sama
            result = subprocess.run(
                [sys.executable, py_file], 
                capture_output=True, 
                text=True,
                encoding='utf-8',
                errors='replace'
            )

            output_filename = filename.replace(".py", "_result.txt")
            output_path = os.path.join(RESULTS_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"--- EXECUTION REPORT FOR: {filename} ---\n")
                f.write(f"--- SOURCE: {py_file} ---\n\n")
                
                if result.returncode == 0:
                    f.write("STATUS: SUCCESS\n")
                    f.write("="*30 + "\n\n")
                    f.write(result.stdout)
                else:
                    f.write("STATUS: FAILED\n")
                    f.write("="*30 + "\n\n")
                    f.write("ERROR LOGS:\n")
                    f.write(result.stderr)
                    f.write("\nPARTIAL OUTPUT:\n")
                    f.write(result.stdout)

            print(f"   [OK] Saved output to: {output_path}")

        except Exception as e:
            print(f"   [ERR] Error running subprocess: {e}")

    print("\n" + "="*30)
    print("ALL EXECUTIONS COMPLETED")
    print(f"Check the '{RESULTS_DIR}' folder for graph visualizations and logs.")
    print("="*30)

if __name__ == "__main__":
    main()