# 🧰 PolicyForge – Générateur de Politiques de Sécurité IA

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Security-Rules_Generator-red.svg?style=for-the-badge&logo=shield&logoColor=white" alt="Security Rules Generator"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License: MIT"/>
</p>

<p align="center">
  <b>Automatisation de la création de règles de sécurité basée sur l'analyse de logs</b><br>
  <sub>📊 Analyse de patterns | 🧠 Détection comportementale | 🛡️ Génération de règles</sub>
</p>

---

## 📋 Description

**PolicyForge** est un outil en ligne de commande qui analyse les fichiers de logs pour identifier les comportements récurrents et générer automatiquement des règles de sécurité dans différents formats standards (Sigma, YARA, iptables). Il permet aux équipes de sécurité d'accélérer la création de règles de détection et de protection basées sur des analyses de comportements réels.

> ⚠️ **Note** : Cet outil est destiné aux professionnels de la sécurité et aux administrateurs système qui souhaitent automatiser la création de règles de sécurité à partir de données réelles.

### 🔍 Fonctionnalités principales

- 📊 **Analyse de logs** (EDR, Web, Cloud, Syslog, JSON)
- 🧠 **Détection automatique** des comportements dominants
- 🧬 **Extraction de patterns** d'activités suspectes
- 📝 **Génération de règles** dans différents formats :
  - ✅ **Sigma** (règles pour SIEM)
  - ✅ **YARA** (règles pour analyse de fichiers)
  - ✅ **iptables** (règles de pare-feu)
- 🔄 **Templates personnalisables** avec Jinja2

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/servais1983/PolicyForge.git
cd PolicyForge

# Rendre le script d'installation exécutable
chmod +x install.sh

# Lancer l'installation
./install.sh
```

## 🛠️ Utilisation

### Génération de règles Sigma

```bash
python3 policyforge.py --logfile examples/logs.json --type sigma
```

### Génération de règles YARA

```bash
python3 policyforge.py --logfile examples/logs.json --type yara
```

### Génération de règles iptables

```bash
python3 policyforge.py --logfile examples/logs.json --type iptables
```

### Exemples de résultats

#### Règle Sigma

```yaml
title: Suspicious URI Access
logsource:
  product: webserver
detection:
  selection:
    uri|contains: "/admin/login.php"
  condition: selection
level: medium
```

#### Règle YARA

```
rule SuspiciousCommand_powershell_Command_Invoke_WebRequest
{
  strings:
    $cmd = "powershell -Command \"Invoke-WebRequest http://malicious.example.com\""
  condition:
    $cmd
}
```

#### Règle iptables

```
-A INPUT -s 192.168.1.100 -j DROP
```

## 🗂️ Structure du projet

```
policyforge/
├── core/                  # Modules principaux
│   ├── parser.py          # Analyse des logs
│   ├── profiles.py        # Détection de patterns / comportements
│   ├── generator.py       # Génération de règles via templates
│   ├── templates/         # Modèles Jinja2
│   │   ├── iptables.j2    # Template pour règles iptables
│   │   ├── sigma.j2       # Template pour règles Sigma
│   │   └── yara.j2        # Template pour règles YARA
│   └── utils.py           # Fonctions utilitaires
├── examples/              # Exemples de logs
│   └── logs.json          # Logs d'exemple pour tests
├── policyforge.py         # Interface CLI principale
├── requirements.txt       # Dépendances Python
├── install.sh             # Script d'installation
└── README.md              # Documentation
```

## 🔮 Roadmap

Voici les fonctionnalités prévues pour les futures versions :

- [ ] **Génération de règles Snort/Suricata** pour les IDS/IPS
- [ ] **Module d'export direct vers Elasticsearch** pour les règles Sigma
- [ ] **Interface web** avec FastAPI pour une utilisation plus conviviale
- [ ] **Prise en charge des logs syslog** et autres formats standards
- [ ] **Meilleure corrélation des événements** pour une détection plus précise
- [ ] **Intégration avec des API de threat intelligence** pour enrichir les règles
- [ ] **Génération de documentation** pour les règles créées
- [ ] **Validation des règles** avant génération finale

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

1. **Ajouter des templates** pour d'autres types de règles
2. **Améliorer les algorithmes de détection** de patterns
3. **Ajouter la prise en charge** d'autres formats de logs
4. **Documenter** des cas d'usage supplémentaires

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---

<p align="center">
  <sub>🔐 Développé pour automatiser la création de défenses basées sur les données réelles</sub>
</p>
