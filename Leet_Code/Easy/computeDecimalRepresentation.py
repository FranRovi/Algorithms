# Leet Code Algo 3697. Compute Decimal Representation.

def decimalRepresentation(n):
    str_n = str(n)
    len_n = len(str(n))
    idx = 1
    temp = [0] * len_n
    for i in range(len_n - 1, -1, -1):
        temp[i] = idx * int(str_n[i])
        idx = int(str(idx) + "0")
    answer = []
    for j in range(len(temp)):
        if temp[j] != 0:
            answer.append(temp[j])
    return answer

print(decimalRepresentation(537))
print(decimalRepresentation(102))
print(decimalRepresentation(6))