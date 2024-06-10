from sympy import mod_inverse

# Fonction pour convertir un nombre entier en texte
def int_to_text(number):
    text = ''
    while number > 0:
        text = chr(number % 256) + text
        number //= 256
    return text

# Valeurs données
N = 25203072061613986373945886893335124115493463487628727874031059800822061809567
C = 21370860772767430569952506747247564236090303327355611280955497891572895095762
e = 65537

# Facteurs de N
p = 158754754453572149934540516805858365529
q = 158754754453572149934540516805858365623
phi_N = (p - 1) * (q - 1)

# Calcul de d
d = mod_inverse(e, phi_N)

# Déchiffrement du message
M = pow(C, d, N)

# Conversion du message déchiffré en texte
message_text = int_to_text(M)
print(message_text)

