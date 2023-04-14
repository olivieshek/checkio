# пешка на границе - нет больше рядов
def safe_pawns(pawns: set) -> int:
    coords = list()
    safe = 0
    for pawn in pawns:
        coords.append(str(ord(pawn[0]) - 97) + pawn[1])
    for coord in coords:
        if int(str(int(str(coord)[0] - 1)) + str(int(str(coord)[1]) - 1)) in coords or int(str(int(str(coord)[0] + 1)) + str(int(str(coord)[1]) - 1)) in coords:
            safe += 1
    return safe
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


    # TODO: через перевод из ord в char