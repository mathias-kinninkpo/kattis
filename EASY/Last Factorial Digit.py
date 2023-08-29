def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
for i in range(int(input())):
    n=int(input())
    print(str(fact(n))[-1])