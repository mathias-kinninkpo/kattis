p = int(input())
response = {}
for _ in range(p):
    k, n = map(int, input().split())
    for i in range(n):
        if k in response.keys():
            response[k] = response[k] + i+2
        else:
            response[k] = i+2
for k, b in response.items():
    print(k, b)
    