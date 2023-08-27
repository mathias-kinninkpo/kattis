grades = list()
for i in range(5):
    grades.append(sum(map(int, input().split())))
    
print(grades.index(max(grades)) + 1, max(grades))