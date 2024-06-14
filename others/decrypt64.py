import base64

# La chaîne encodée en Base64 trouvée dans le meta
encoded_str = "ApvK67ociHgr2egd6c2ZjrfPuRs8BHcvSggogIOPQNH7GJ3cVlyJ1NOq/COCdj0+zxskqHt9HgLLETc8qqD+vwsAAABteyJvcmlnaW4iOiJodHRwczovL3lvdXR1YmUuY29tOjQ0MyIsImZlYXR1cmUiOiJQcml2YWN5U2FuZGJveEFkc0FQSXMiLCJleHBpcnkiOjE2OTUxNjc5OTksImlzU3ViZG9tYWluIjp0cnVlfQ=="

def is_base64(s):
    try:
        # Vérifie si la chaîne peut être décodée correctement
        if base64.b64encode(base64.b64decode(s)).decode('utf-8') == s:
            return True
    except Exception:
        return False
    return False

def decode_base64_recursive(encoded_str):
    decoded_str = encoded_str
    while is_base64(decoded_str):
        decoded_bytes = base64.b64decode(decoded_str)
        try:
            decoded_str = decoded_bytes.decode('utf-8')
        except UnicodeDecodeError:
            decoded_str = decoded_bytes.decode('ISO-8859-1')
    return decoded_str

# Appeler la fonction et imprimer le résultat final
final_result = decode_base64_recursive(encoded_str)
print(final_result)

