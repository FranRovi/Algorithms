# Leet Code Algo 1556. Thousand Separator.

def thousandSeparator(n):
    num_str = str(n)
    if n < 1000:
        return num_str
    len_num_str = len(num_str)
    counter = 0
    answer = ""
    for i in range(len_num_str-1,-1,-1):
        if counter == 3:
            answer = num_str[i] + "." + answer
            counter = 0
        else:
            answer = num_str[i] + answer
        counter += 1
    return answer

print(thousandSeparator(987))
print(thousandSeparator(1234))