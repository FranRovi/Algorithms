# Hacker Rank Library Fine

def libraryFine(d1, m1, y1, d2, m2, y2):
    # 1 <= d2 and m1 <= m2 and y1 <= y2 or
    if (y1 < y2) or (d1 <= d2 and m1 <= m2 and y1 <= y2) or (y1 <= y2 and m1 < m2):
        return 0
    elif m1 <= m2 and y1 <= y2 and d1 > d2:
        return (d1 - d2) * 15
    elif y1 <= y2 and m1 > m2:
        return (m1 - m2) * 500
    else:
        return 10000
print(libraryFine(14, 7, 2018, 5, 7, 2018))
print(libraryFine(9, 6, 2015, 6, 6, 2015))
print(libraryFine(2, 7, 1014, 1, 1, 1015))
print(libraryFine(28, 2, 2015, 15, 4, 2015))