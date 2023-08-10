
def move( x, y):

    if (x == 1):
        if (y == 'A') :return 2
        elif (y == 'B'): return 1
        else: return 3
    
    if (x == 2):
        if (y == 'A'): return 1
        elif (y == 'B'): return 3
        else :return 2
    
    if (x == 3):
        if (y == 'A'): return 3
        elif (y == 'B'): return 2
        else: return 1
    

chaine = input()
position = 1
for c in chaine:
    position = move(position, c)
print(position)