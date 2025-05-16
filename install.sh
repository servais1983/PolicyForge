#!/bin/bash
echo "[*] Installation de PolicyForge..."

sudo apt update
sudo apt install -y python3 python3-pip
pip install -r requirements.txt

echo "[✓] PolicyForge prêt. Exemple :"
echo "python3 policyforge.py --logfile examples/logs.json --type sigma"