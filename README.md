# Agentic AI Framework Generator (Group 5)

Tools ini secara otomatis mengonversi pola **Agentic AI** dari format Knowledge Graph (RDF) menjadi kode kerangka kerja yang dapat dieksekusi untuk **LangGraph (Python)** dan **Mastra AI (TypeScript)**.

Proyek ini dibuat untuk memenuhi tugas mata kuliah Agentic AI Framework berdasarkan paper *K-CAP 2025*.

## Fitur Utama
- **Dual Output Generation:** Menghasilkan kode Python (LangGraph) dan TypeScript (Mastra) sekaligus dari satu sumber RDF.
- **Robust Extraction:** Mampu menangani file RDF dengan atau tanpa header prefix standar.
- **Runnable Code:** Kode hasil generate dilengkapi blok eksekusi, simulasi state (LangGraph), dan bypass typing (Mastra) agar langsung bisa dijalankan.
- **Synthetic Data Generator:** Termasuk script untuk menghasilkan pola dummy guna pengujian skala besar (25+ pola).

## Struktur Folder
- `input_rdfs/`: Tempat menaruh file .rdf (sumber Knowledge Graph).
- `output_frameworks/`: Hasil generate kode LangGraph (.py).
- `mastra_project/`: Hasil generate kode Mastra (.ts) yang siap eksekusi.
- `extractor.py`: Modul parsing RDF.
- `codegen.py`: Modul template generator (Python & TypeScript).

## Cara Menjalankan

### 1. Prasyarat
- Python 3.8+
- Node.js & npm (untuk Mastra)
- Library Python: `rdflib`
- Library Node: `tsx`

### 2. Generate Framework
Jalankan perintah ini untuk memproses semua RDF di `input_rdfs`:
```
python main.py
```
3. Menjalankan Hasil (Demo)
LangGraph (Python):
```
python output_frameworks/langgraph/customer_support_langgraph.py
```
Mastra AI (TypeScript):
```
cd mastra_project
npx tsx customer_support_mastra.ts
```
