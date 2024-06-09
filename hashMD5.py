import hashlib

def calculate_md5_hash(input_string):
    # Convertir la chaîne en bytes (UTF-8)
    byte_string = input_string.encode('utf-8')

    # Calculer le hash MD5
    md5_hash = hashlib.md5(byte_string)

    # Récupérer la représentation hexadécimale du hash
    hex_hash = md5_hash.hexdigest()

    return hex_hash

# Exemple d'utilisation : calculer le hash MD5 d'une chaîne
input_string = input()
md5_result = calculate_md5_hash(input_string)

print("Chaîne d'entrée :", input_string)
print("Hash MD5 :", md5_result)

