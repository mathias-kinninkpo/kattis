def median(l):
    return sorted(l)[1]
# def transpose(l):
#     liste = list()
#     for i in range(len(l)):
#         for j in range(len(l[0])):
#             liste.append()

liste = list()
n = int(input())
for i in range(3):
    liste.append(list(map(int, input().split())))
med = list()
for i in range(n):
    med.append(median([liste[0][i],liste[1][i], liste[2][i]]))
print(*med)