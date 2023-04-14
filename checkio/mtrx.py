# mtrx = [[0] * 8] * 8
# chess = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
# print(*mtrx, sep='\n')
# for i in chess:
#     mtrx[int(i[1])][ord(i[0]) - 97] = 1
# print(*mtrx, sep='\n')

# for i in chess:
#     mtrx

pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}

for pawn in pawns:
    coords = list()
    mtrx = [[0] * 8] * 8
    for pawn in pawns:
        coords.append(str(ord(pawn[0]) - 97) + pawn[1])
    for i in coords:
        


print(coords)
print(*mtrx, sep='\n')