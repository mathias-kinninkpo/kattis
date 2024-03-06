monney = {
    "Monnei": int(input()),
    "Fjee": int(input()),
    "Dolladollabilljoll": int(input())
}

print(min(monney.items(), key=lambda x : x[1])[0])