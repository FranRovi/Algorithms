# Leet Code Algo 3798. Largest Even Number

def largestEven(s):
    max_even_num = 0
    idx = 0
    len_s = len(s)
    temp = ""
    for i in range(len_s):
        temp = s[:len_s - idx]
        temp_int = int(temp)
        idx += 1

        if temp_int % 2 == 0 and temp_int > max_even_num:
            max_even_num = temp_int
            break 

    return "" if max_even_num == 0 else str(max_even_num)

print(largestEven("1112"))
print(largestEven("221"))
print(largestEven("1"))
print(largestEven("2"))
print(largestEven("21"))