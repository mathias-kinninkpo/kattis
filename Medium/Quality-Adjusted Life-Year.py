life = 0
for i in range(int(input())):
    a,b = map(float, input().split())
    life += (a*b)
print(life)