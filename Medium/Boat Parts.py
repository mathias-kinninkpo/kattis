p,n = map(int, input().split())
piece = list()
ended = False
days = 0
for _ in range(n):
    piece.append(input())
    if ended: continue
    if len(set(piece)) == p:
        days = _ + 1
        ended = True
    
if not ended:
    print("paradox avoided")
else:print(days)
