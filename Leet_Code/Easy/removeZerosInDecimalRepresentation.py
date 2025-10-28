# Leet Code Algo 3726. Remove Zeros in Decimal Representation.

def removeZeros(n):
    list_arr = []
    str_num = str(n)
    for char in str_num:
        if int(char) != 0:
            list_arr.append(char)
    temp = "".join(list_arr)
    return int(temp)


print(removeZeros(1020030))
print(removeZeros(1))