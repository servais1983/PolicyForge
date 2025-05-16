from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("core/templates"))

def generate(rule_type, patterns):
    template = env.get_template(f"{rule_type}.j2")
    rules = []
    if rule_type == "iptables":
        for ip, _ in patterns["top_ips"]:
            rules.append(template.render(ip=ip))
    elif rule_type == "sigma":
        for uri, _ in patterns["top_uris"]:
            rules.append(template.render(uri=uri))
    elif rule_type == "yara":
        for cmd, _ in patterns["top_cmds"]:
            rules.append(template.render(cmd=cmd))
    return rules