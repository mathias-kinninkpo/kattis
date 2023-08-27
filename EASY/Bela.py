mat = {"A":(11,11), "K":(4,4), "Q":(3,3), "J":(20,2),"T":(10,10),"9":(14,0),"8":(0,0),"7":(0,0)}
n,s = map(str, input().split())
som = 0
for i in range(4*int(n)):
    ch = input()
    if ch[1] == s:
        som += mat[ch[0]][0]
    else:
        som += mat[ch[0]][1]
print(som)
