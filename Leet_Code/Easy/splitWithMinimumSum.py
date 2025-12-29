# Leet Code Algo 2578. Split With Minimum Sum

def splitNum(num):
    num_arr = list(str(num))
    sorted_num_arr = sorted(num_arr)
    num_one_arr = []
    num_two_arr = []
    for i in range(len(sorted_num_arr)):
        if i % 2 == 0:
            num_one_arr.append(sorted_num_arr[i])
        else:
            num_two_arr.append(sorted_num_arr[i])
    num_one = ""
    for num in num_one_arr:
        num_one += num
    num_two = ""
    for num in num_two_arr:
        num_two += num
    return(int(num_one) + int(num_two))

print(splitNum(4325))
print(splitNum(687))
print(splitNum(11))
print(splitNum(999999999))
print(splitNum(100001))