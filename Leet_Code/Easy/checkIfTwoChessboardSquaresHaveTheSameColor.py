# Leet Code Algo 3274. Check if Two ChessBoard Squares Have The Same Color

def checkTwoChessboards(coordinate1, coordinate2):
    hash_letter = { "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8 }

    if ((hash_letter[coordinate1[0]] % 2 != 0 and int(coordinate1[1]) % 2 != 0) and
    (hash_letter[coordinate2[0]] % 2 != 0 and int(coordinate2[1]) % 2 != 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 == 0 and int(coordinate1[1]) % 2 == 0) and
    (hash_letter[coordinate2[0]] % 2 == 0 and int(coordinate2[1]) % 2 == 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 != 0 and int(coordinate1[1]) % 2 == 0) and
    (hash_letter[coordinate2[0]] % 2 != 0 and int(coordinate2[1]) % 2 == 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 == 0 and int(coordinate1[1]) % 2 != 0) and
    (hash_letter[coordinate2[0]] % 2 == 0 and int(coordinate2[1]) % 2 != 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 == 0 and int(coordinate1[1]) % 2 != 0) and
    (hash_letter[coordinate2[0]] % 2 != 0 and int(coordinate2[1]) % 2 == 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 != 0 and int(coordinate1[1]) % 2 == 0) and
    (hash_letter[coordinate2[0]] % 2 == 0 and int(coordinate2[1]) % 2 != 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 == 0 and int(coordinate1[1]) % 2 == 0) and
    (hash_letter[coordinate2[0]] % 2 != 0 and int(coordinate2[1]) % 2 != 0)):
        return True
    if ((hash_letter[coordinate1[0]] % 2 != 0 and int(coordinate1[1]) % 2 != 0) and
    (hash_letter[coordinate2[0]] % 2 == 0 and int(coordinate2[1]) % 2 == 0)):
        return True
    return False

print(checkTwoChessboards("a1", "c3"))
print(checkTwoChessboards("a1", "h3"))
print(checkTwoChessboards("c2", "g4"))
print(checkTwoChessboards("h7", "c8"))
print(checkTwoChessboards("c8", "b3"))
print(checkTwoChessboards("b2", "g7"))
print(checkTwoChessboards("a5", "h4"))