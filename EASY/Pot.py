def exp(value):
    return int(value[:-1])**int(value[-1])
x = 0
for i in range(int(input())):
    x += exp(input())
print(x)

