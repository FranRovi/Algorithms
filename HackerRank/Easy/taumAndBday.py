# Hacker Rank Algo Taum and B'Day

def taumBday(b, w, bc, wc, z):
    cheapestB = bc if bc < wc + z else wc + z
    cheapestW = wc if wc < bc + z else bc + z
    
    return b * cheapestB + w * cheapestW

# print(taumBday(3, 5, 3, 4, 1))
print(taumBday(10, 10, 1, 1, 1))
print(taumBday(5, 9, 2, 3, 4))
print(taumBday(3, 6, 9, 1, 1))
print(taumBday(7, 7, 4, 2, 1))
print(taumBday(3, 3, 1, 9, 2))
