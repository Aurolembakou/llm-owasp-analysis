import os
from openai import OpenAI

# Récupération de la clé depuis la variable d'environnement
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Envoi d'une requête simple pour tester l'accès à l'API
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Affichage de la réponse du modèle
print(response.choices[0].message.content)
