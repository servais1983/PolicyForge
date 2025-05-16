from collections import Counter

def extract_patterns(logs):
    sources = [log.get("src_ip") for log in logs if "src_ip" in log]
    commands = [log.get("command") for log in logs if "command" in log]
    uris = [log.get("uri") for log in logs if "uri" in log]

    return {
        "top_ips": Counter(sources).most_common(3),
        "top_cmds": Counter(commands).most_common(3),
        "top_uris": Counter(uris).most_common(3)
    }