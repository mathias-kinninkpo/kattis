import email
from email import policy
from email.parser import BytesParser

# Lire le fichier .eml
with open("spam.eml", "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

# Extraire le corps du mail
if msg.is_multipart():
    for part in msg.iter_parts():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
else:
    body = msg.get_payload(decode=True).decode()

# Afficher le corps du mail
print(body)

# Recherche d'un flag potentiel dans le corps du mail
import re

flag = re.findall(r'FLAG\{.*?\}', body)
if flag:
    print("Flag trouvé :", flag)
else:
    print("Aucun flag trouvé")

