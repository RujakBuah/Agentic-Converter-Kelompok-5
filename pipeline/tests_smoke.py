import os, json, glob

OUT = "examples/generated"
REPORT = "reports/checklist_week2.md"

def check_generated():
    results = []
    mastra_dirs = glob.glob(os.path.join(OUT, "mastra", "*"))

    for md in mastra_dirs:
        pattern = os.path.basename(md)
        assistant = os.path.join(md, "assistant.ts")
        lg = os.path.join(OUT, "langgraph", pattern, "graph.json")

        entry = {
            "pattern": pattern,
            "assistant_exists": os.path.exists(assistant),
            "langgraph_exists": os.path.exists(lg)
        }

        if entry["langgraph_exists"]:
            try:
                with open(lg, "r", encoding="utf-8") as f:
                    data = json.load(f)
                entry["json_valid"] = True
                entry["nodes_count"] = len(data.get("nodes", []))
            except Exception as e:
                entry["json_valid"] = False
                entry["json_error"] = str(e)

        results.append(entry)

    return results


def write_report(results):
    os.makedirs("reports", exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("# Week2 checklist results\n\n")
        for r in results:
            f.write(f"## Pattern: {r['pattern']}\n")
            f.write(f"- assistant.ts exists: {r['assistant_exists']}\n")
            f.write(f"- graph.json exists: {r['langgraph_exists']}\n")
            f.write(f"- graph.json valid: {r.get('json_valid')}\n")
            f.write(f"- nodes count: {r.get('nodes_count')}\n\n")

    print("Wrote report to", REPORT)


if __name__ == "__main__":
    res = check_generated()
    write_report(res)