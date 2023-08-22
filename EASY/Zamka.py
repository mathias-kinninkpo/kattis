def check(a):
    return sum([int(i) for i in a])
l = int(input())
d = int(input())
lis = list(range(l,d+1))
x = int(input())
for i in lis:
    a = check(str(i))
    if a == x:
        print(i)
        break
for i in lis[::-1]:
    a = check(str(i))
    if a == x:
        print(i)
        break
