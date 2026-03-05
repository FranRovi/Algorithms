# Leet Code Algo 1417. Reformat The String

def reformat(s):
    arr_chars = []
    arr_nums = []
    answer = ""
    for char in s:
        if char.isdigit():
            arr_nums.append(char)
        else:
            arr_chars.append(char)
    len_chars = len(arr_chars)
    len_nums = len(arr_nums)
    if len_nums + 1 == len_chars or len_nums - 1 == len_chars or len_nums == len_chars:
        smallest = 0
        largest = 0
        if len_chars >= len_nums:
            largest = arr_chars
            smallest = arr_nums
        else:
            largest = arr_nums
            smallest = arr_chars
        
        for i in range(len(smallest)):
            answer += largest[i]
            answer += smallest[i]
        if len(largest) != len(smallest):
            answer += largest[-1]
    else:
        return ""
    return answer

print(reformat("a0b1c2"))
print(reformat("leetcode"))
print(reformat("1229857369"))
print(reformat("covid2019"))

