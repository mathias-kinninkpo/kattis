s,t,n = map(int, input().split())
wl = list(map(int, input().split()))
dur = list(map(int, input().split()))
ar = list(map(int, input().split()))
h = s
for i in range(n):
    h += max(wl[i],ar[i]) + dur[i]
print("yes" if h + wl[n] <= t else "no")