# Fonctions utilitaires pour PolicyForge

import os
import re
import json

def ensure_directory(path):
    """S'assure qu'un répertoire existe, le crée si nécessaire."""
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def sanitize_filename(name):
    """Nettoie une chaîne pour en faire un nom de fichier valide."""
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', name)

def save_rules(rules, rule_type, output_dir="output"):
    """Sauvegarde les règles générées dans des fichiers."""
    ensure_directory(output_dir)
    
    for i, rule in enumerate(rules):
        filename = f"{rule_type}_rule_{i+1}.{get_extension(rule_type)}"
        path = os.path.join(output_dir, filename)
        
        with open(path, 'w') as f:
            f.write(rule)
            
    return len(rules)

def get_extension(rule_type):
    """Retourne l'extension appropriée selon le type de règle."""
    extensions = {
        "sigma": "yml",
        "yara": "yar",
        "iptables": "sh"
    }
    return extensions.get(rule_type, "txt")