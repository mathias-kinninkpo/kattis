n = int(input())
print(*list(set(list(map(int, input().split()))) - set(list(map(int, input().split())))))