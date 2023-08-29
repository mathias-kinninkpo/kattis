def diag(n,m):
    return (n**2 + m**2)**0.5

a, b, c = map(int, input().split())

for i in range(a):
    print("DA" if diag(b,c) >= int(input()) else "NE")