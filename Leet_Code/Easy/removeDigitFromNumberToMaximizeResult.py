# Leet Code Algo 2259. Remove Digit From Number To Maximize Result

def removeDigit(number, digit):
    list_num = list(number)
    hash_position = {}
    hash_position[digit] = []
    for i in range(len(list_num)):
        if list_num[i] == digit:
            hash_position[digit].append(i)
    values = hash_position[digit]
    answer = []
    for j in range(len(values)):
        copy_list_num = list(number)
        del copy_list_num[values[j]]
        temp_num_str = "".join(copy_list_num)
        answer.append(temp_num_str)
    sorted_answer = sorted(answer, reverse = True)
    return sorted_answer[0]

print(removeDigit("123", "3"))
print(removeDigit("1231", "1"))
print(removeDigit("551", "5"))
print(removeDigit("133235", "3"))