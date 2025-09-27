# Leet Code Algo 2027. Minimum Moves To Convert String

def minimumMoves(s):
    arr_s = list(s)
    idx = 0
    counter = 0
    while idx < len(s) - 2:
        if arr_s[idx] == "X":
            arr_s[idx] = "O"
            arr_s[idx+1] = "O"
            arr_s[idx+2] = "O"
            counter += 1
            idx += 2
        else:
            idx += 1
    if arr_s[-1] == "X" or arr_s[-2] == "X":
        counter += 1
    return counter

print(minimumMoves("XXX"))
print(minimumMoves("XXOX"))
print(minimumMoves("OOOO"))
print(minimumMoves("OOOOXXXOXO"))