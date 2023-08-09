a,b = input(), input()
M = list(map(int,input().split()))
N = list(map(int,input().split()))
dif = [abs(c-d) for c,d in zip(M,N)]
occ = [dif.count(i) for i in dif]
print(dif[occ.index(max(occ))])

