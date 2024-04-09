# Hacker Rank Algo Halloween Sale

def halloweenSale(p, d, m, s):
    counter = 0
    currGamePrice = p
    if p > s:
        return counter
    while s >= p:
        # print(s, currGamePrice, p)
        counter += 1
        currGamePrice = p - d
        s -= p
        if currGamePrice >= m:
            p -= d
        if m > currGamePrice:
            p = m
    return counter


# counter = 0
#     if p > s:
#         return counter
#     while s >= m:
#         counter += 1
#         s -= p
#         if p >= m:
#             p -= d
#         if m > p:
#             p = m
#     return counter

print(halloweenSale(20, 3, 6, 70)) 
print(halloweenSale(20, 3, 6, 80))
print(halloweenSale(20, 3, 6, 85))
print(halloweenSale(100, 1, 1, 99)) # expected 0
print(halloweenSale(100, 19, 1, 180)) # expected 1
print(halloweenSale(100, 12, 55, 95)) # expected 0      