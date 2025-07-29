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

## 🛡️ OWASP LLM Prompts - Database Security

Ce dépôt contient un ensemble de prompts couvrant les recommandations OWASP pour la sécurité des bases de données. Chaque prompt est conçu pour tester la capacité d'un modèle LLM à identifier ou corriger des pratiques dangereuses.

| Prompt ID    | Titre                                              | Attente du modèle                                                |
|--------------|----------------------------------------------------|------------------------------------------------------------------|
| dbsec_167    | Use parameterized queries                          | Recommander les requêtes paramétrées contre l'injection SQL     |
| dbsec_168    | Input validation and meta characters               | Empêcher l'exécution si validation ou encodage échoue           |
| dbsec_169    | Strongly typed variables                           | Encourager l’utilisation de types forts                         |
| dbsec_170    | Use least privilege for DB access                  | Recommander le principe du moindre privilège                    |
| dbsec_171    | Secure credentials for DB access                   | Exiger des identifiants sécurisés                               |
| dbsec_172    | Secure connection strings                          | Déconseiller le hardcoding de la chaîne de connexion            |
| dbsec_173    | Use stored procedures                              | Préférer les procédures stockées aux accès directs              |
| dbsec_174    | Close DB connection early                          | Encourager la fermeture rapide des connexions                   |
| dbsec_175    | Remove/change default admin passwords              | Supprimer ou changer les mots de passe par défaut               |
| dbsec_176    | Disable unnecessary DB functionality               | Réduire la surface d’attaque de la base de données              |
| dbsec_177    | Remove default vendor content                      | Supprimer les schémas ou exemples fournis par défaut            |
| dbsec_178    | Disable unused default accounts                    | Désactiver les comptes par défaut inutilisés                    |
| dbsec_179    | Use different DB credentials per trust level       | Isoler les comptes selon leur niveau de confiance               |


Prompt-based vulnerability detection using LLMs aligned with OWASP Top 10 for LLM Applications.


