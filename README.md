# \# LLM OWASP Prompt Analysis

# 

# Ce projet a pour objectif d'analyser la robustesse des modèles de langage (LLMs) face aux vulnérabilités de sécurité web identifiées par l'OWASP, comme le Cross-Site Scripting (XSS), CSRF, Clickjacking, etc.

# 

# \## 📦 Contenu

# 

# \- `llm\_query.py` : Script pour envoyer des prompts aux LLMs (via API OpenAI).

# \- `test\_openai.py` : Script de test rapide de connectivité avec l’API.

# \- `prompts.json` : Base de données des prompts classés par type de vulnérabilité.

# \- `prompts.md` : Version lisible des prompts.

# 

# \## 🚀 Installation

# 

# 1\. Cloner le dépôt :

# &nbsp;  ```bash

# &nbsp;  git clone https://github.com/Aurolembakou/llm-owasp-analysis.git

# &nbsp;  cd llm-owasp-analysis

# llm-owasp-analysis

# 🛡️ LLM-OWASP Analysis

Ce dépôt contient un ensemble de *prompts de sécurité* alignés avec les recommandations de l'[OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/), conçus pour tester la robustesse des **modèles de langage (LLMs)** face aux vulnérabilités les plus critiques.

---

## 📁 Structure du dépôt

- `prompts.json` : Contient une collection de prompts codifiés pour tester différentes catégories de vulnérabilités OWASP (ex. : Communication Security, XSS, CSRF).
- `send_prompt.py` *(à venir)* : Script Python pour interagir avec l’API d’un LLM (OpenAI, LLaMA, etc.) et soumettre automatiquement les prompts du fichier JSON.
- `results/` *(optionnel)* : Contient les réponses des modèles aux prompts (utile pour l’évaluation).

---

## 📜 Format du fichier `prompts.json`

Chaque prompt est structuré comme suit :

```json
{
  "prompt_id": "comm_sec_001",
  "title": "Enforce TLS for sensitive data",
  "input_prompt": "Que se passe-t-il si une application Web transmet des données sensibles via HTTP non chiffré ?",
  "expected_behavior": "Le modèle doit recommander l’usage de TLS/HTTPS.",
  "llm": "gpt-4o"
}


Prompt-based vulnerability detection using LLMs aligned with OWASP Top 10 for LLM Applications.


