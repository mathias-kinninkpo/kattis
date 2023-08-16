inter = set()
isright = False
for i in range(int(input())):
    a,b = map(int,input().split())
    inte1 = set(list(range(a,b+1)))
    if i == 0: inter = inter | inte1
    inter = inter & inte1 

if inter != set():
    print("gunilla has a point")
else: print("edward is right")
    