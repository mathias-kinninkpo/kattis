def letter(bord):
    if bord[0] == bord[1] and bord[1] == bord[2] and bord[0] == bord[2]:
        return bord[0]
    if bord[3] == bord[4] and bord[5] == bord[4] and bord[5] == bord[3]:
        return bord[3]
    if bord[6] == bord[7] and bord[6] == bord[8] and bord[7] == bord[6]:
        return bord[6]
    if bord[0] == bord[3] and bord[0] == bord[6] and bord[3] == bord[6]:
        return bord[0]
    if bord[1] == bord[4] and bord[1] == bord[7] and bord[4] == bord[7]:
        return bord[1]
    if bord[2] == bord[8] and bord[5] == bord[8] and bord[2] == bord[5]:
        return bord[2]
    if bord[0] == bord[4] and bord[8] == bord[4] and bord[0] == bord[8]:
        return bord[0]
    if bord[2] == bord[4] and bord[6] == bord[4] and bord[6] == bord[2]:
        return bord[2]
    else: return '_'



board = []
for i in range(3):
    for j in input().split(' '):
        board.append(j)


if letter(board) == '_':print("ingen har vunnit")
elif letter(board) == 'X':print("Johan har vunnit")
else:print("Abdullah har vunnit")
