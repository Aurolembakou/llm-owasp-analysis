# 🔐 OWASP LLM Prompt Repository - Aurolembakou

Ce dépôt contient un ensemble de prompts structurés basés sur les recommandations de l’[OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) afin d’évaluer la capacité des modèles de langage (LLMs) à identifier ou suggérer des solutions de sécurité.  

Le fichier principal `prompts.json` permet une exploitation automatisée avec l'API OpenAI pour tester GPT-4o, GPT-4, LLaMA, Gemini, et DeepSeek.

---

## 📂 Structure du fichier `prompts.json`

Chaque prompt contient les champs suivants :
- `prompt_id` : Identifiant unique (ex : `comm_143`)
- `title` : Titre explicite du test
- `input_prompt` : Message envoyé au modèle
- `expected_behavior` : Comportement attendu (ce que le modèle devrait répondre)
- `llm` : Modèle de langage testé (GPT-4o, etc.)

---

## 📋 Tableau des prompts OWASP

| Prompt ID      | Catégorie              | Description courte                                                | LLM        |
|----------------|------------------------|-------------------------------------------------------------------|------------|
| xss_001        | XSS                    | Détection XSS dans un champ `<input>`                            | gpt-4o     |
| comm_143       | Communication Security | TLS pour info sensible                                            | gpt-4o     |
| comm_144       | Communication Security | Validité des certificats TLS                                      | gpt-4o     |
| comm_145       | Communication Security | Ne pas faire de fallback HTTP                                     | gpt-4o     |
| comm_146       | Communication Security | TLS obligatoire pour contenu authentifié                          | gpt-4o     |
| comm_147       | Communication Security | TLS vers API externe                                              | gpt-4o     |
| comm_148       | Communication Security | Implémentation TLS unique                                         | gpt-4o     |
| comm_149       | Communication Security | Spécification d’encodage                                          | gpt-4o     |
| comm_150       | Communication Security | Nettoyage des headers Referer                                     | gpt-4o     |
| dbsec_167      | Database Security      | Requêtes paramétrées                                              | gpt-4o     |
| dbsec_168      | Database Security      | Validation des entrées                                            | gpt-4o     |
| dbsec_169      | Database Security      | Typage fort                                                       | gpt-4o     |
| dbsec_170      | Database Security      | Accès avec privilège minimal                                      | gpt-4o     |
| dbsec_171      | Database Security      | Utiliser des identifiants sécurisés                               | gpt-4o     |
| dbsec_172      | Database Security      | Chaînes de connexion non hardcodées                               | gpt-4o     |
| dbsec_173      | Database Security      | Utilisation de procédures stockées                                | gpt-4o     |
| dbsec_174      | Database Security      | Fermeture rapide des connexions                                   | gpt-4o     |
| dbsec_175      | Database Security      | Changement des mots de passe par défaut                           | gpt-4o     |
| dbsec_176      | Database Security      | Réduction de la surface d’attaque des bases de données            | gpt-4o     |
| dbsec_177      | Database Security      | Suppression des schémas par défaut                                | gpt-4o     |
| dbsec_178      | Database Security      | Désactivation des comptes inutiles                                | gpt-4o     |
| dbsec_179      | Database Security      | Identifiants distincts par rôle                                   | gpt-4o     |

---

## 🤖 Modèles de langage utilisés

- OpenAI GPT-4o
- OpenAI GPT-4
- Meta LLaMA (local via Ollama)
- Gemini (Google)
- DeepSeek

---

## 📌 Fichier JSON

Le fichier des prompts est accessible ici :  ➡️ [`prompts.json`](./prompts.json)

---

## 🧪 Utilisation des prompts avec Python

Le script Python fourni (dans `test_openai.py`) permet d’envoyer tous les prompts du fichier JSON aux modèles via API OpenAI.  

```bash
python test_openai.py
