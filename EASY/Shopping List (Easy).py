a,b = map(int, input().split())
en = set(input().split())
for i in range(a-1):
    en = en & set(input().split())
print(len(en))
for i in sorted(list(en)):
    print(i)