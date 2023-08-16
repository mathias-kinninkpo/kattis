n,k = map(int, input().split())
col = list(map(int,input().split()))
z = list()
for i in range(k):
    if i+1 not in col:
        z.append(i+1)
lf = list(filter(lambda x: col.count(x) == 1, col))
if len(z) == 0:
    print(len(lf))
    print(*sorted(lf))
else:
    print(len(z))
    print(*sorted(z))