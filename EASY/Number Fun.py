for i in range(int(input())):
    a, b, c = map(int, input().split())
    print('Possible' if any([a + b == c, abs(a - b) == c, a * b == c, a / b == c, b / a == c]) else 'Impossible')