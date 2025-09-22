# Leet Code Algo 2165. Smallest Value of the Rearranged Number

def smallestNumber(num):
    if num >=0 and num <= 9:
            return num
    is_negative = False if num >= 0 else True
    str_num = str(num)
    len_str_num = len(str_num)
    hash_num = {}
    if is_negative:
        for i in range(1, len_str_num):
            if str_num[i] not in hash_num:
                hash_num[str_num[i]] = 1
            else:
                hash_num[str_num[i]] += 1
    else:
        for i in range(len_str_num):
            if str_num[i] not in hash_num:
                hash_num[str_num[i]] = 1
            else:
                hash_num[str_num[i]] += 1
    if is_negative:
        sorted_hash = dict(sorted(hash_num.items(), reverse=True))
    else:
        sorted_hash = dict(sorted(hash_num.items()))
    answer_arr = []
    for k, v in sorted_hash.items():
        for j in range(v):
            answer_arr.append(k)
    if answer_arr[0] == "0" and is_negative == False:
        num_of_zeros = 0
        for l in range(len(answer_arr)):
            if answer_arr[l] == "0":
                num_of_zeros += 1
            else:
                break
        answer_arr[0], answer_arr[num_of_zeros] = answer_arr[num_of_zeros], answer_arr[0]
    answer = int("".join(answer_arr))
    if is_negative:
        return answer * -1
    return answer

print(smallestNumber(310))
print(smallestNumber(-7605))
print(smallestNumber(420691337))
print(smallestNumber(63))
print(smallestNumber(5059))
print(smallestNumber(95005))