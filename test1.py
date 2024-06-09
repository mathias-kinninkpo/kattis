import base64

# Le message encodé en Base64
encoded_message = "SExCMjAyNHtGMEluM3VyXzBzSW5UXw=="

# Décodage du message en Base64
decoded_bytes = base64.b64decode(encoded_message)
decoded_message = decoded_bytes.decode('utf-8')

print("Message décodé : ", decoded_message)

