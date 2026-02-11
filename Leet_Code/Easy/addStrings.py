# Leet Code Algo 415. Add Strings

def addStrings(num1, num2):
    arr_num_1 = []
    for n in num1:
        arr_num_1.append(int(n))

    arr_num_2 = []
    for n in num2:
        arr_num_2.append(int(n))

    len_num_1 = len(arr_num_1)
    len_num_2 = len(arr_num_2)
    answer = [0]
    if len_num_1 >= len_num_2:
        answer = [0] * len_num_1
    else:
        answer = [0] * len_num_2

    if len_num_2 > len_num_1:
        for i in range(len_num_2 - len_num_1):
            arr_num_1.insert(0,0)
    else:
        for j in range(len_num_1 - len_num_2):
            arr_num_2.insert(0,0)
    prev = 0
    for k in range(len(arr_num_1) -1, -1, -1):
        temp = arr_num_1[k] + arr_num_2[k]
        if temp + prev <= 9:
            answer[k] = arr_num_1[k] + arr_num_2[k] + prev
            prev = 0
        else:
            answer[k] = (arr_num_1[k] + arr_num_2[k] + prev) % 10
            prev = 1
    if prev == 1:
        answer.insert(0, 1)
    final_num_str = ""
    for n in answer:
        final_num_str += str(n)
    return "".join(final_num_str)

print(addStrings("11", "123"))
print(addStrings("456", "77"))
print(addStrings("0", "0"))