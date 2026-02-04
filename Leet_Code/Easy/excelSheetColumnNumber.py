# Leet Code Algo 171. Excel Sheet Column Number

def titleToNumber(columnTitle):
    hash_letter = {
            "A": 1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,
            "N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26
        }

    total_sum = 0
    idx = 0
    len_title = len(columnTitle) - 1

    for char in columnTitle:
        total_sum += hash_letter[char] * 26 ** (len_title - idx)
        idx += 1
    return total_sum

print(titleToNumber("A"))
print(titleToNumber("AB"))
print(titleToNumber("ZY"))
print(titleToNumber("ZYA"))