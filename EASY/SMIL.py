smil = input()
for i in range(len(smil)-1):
    if smil[i:i+2] == ":)":
        print(i)
    if smil[i:i+2] == ";)":
        print(i)
    if smil[i:i+3] == ":-)":
        print(i)
    if smil[i:i+3] == ";-)":
        print(i)