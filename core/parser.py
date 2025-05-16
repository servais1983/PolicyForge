import json

def load_logs(logfile):
    logs = []
    with open(logfile, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            try:
                logs.append(json.loads(line))
            except:
                logs.append({"raw": line.strip()})
    return logs