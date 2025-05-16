#!/usr/bin/env python3

import argparse
from core import parser, profiles, generator

def main():
    cli = argparse.ArgumentParser(description="PolicyForge - Générateur de règles sécurité IA")
    cli.add_argument("--logfile", required=True, help="Fichier de logs (json, syslog...)")
    cli.add_argument("--type", choices=["sigma", "iptables", "yara"], required=True, help="Type de règle à générer")
    args = cli.parse_args()

    entries = parser.load_logs(args.logfile)
    behaviors = profiles.extract_patterns(entries)
    rules = generator.generate(args.type, behaviors)

    for rule in rules:
        print(f"\n--- Règle générée ({args.type}) ---\n{rule}")

if __name__ == "__main__":
    main()