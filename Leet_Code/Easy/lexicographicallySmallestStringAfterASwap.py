# Leet Code Algo 3216. Lexicographically Smallest String After a Swap.

def getSmallestString(s):
    adjacent_nums = []
    adjacent_nums_idx = []
    s_list = list(s)
    for i in range(1, len(s)):
        if (int(s[i-1]) % 2 == 0 and int(s[i]) % 2 == 0 or
            int(s[i-1]) % 2 != 0 and int(s[i]) % 2 != 0):
            temp = [s[i-1], s[i]]
            temp_idx = [i-1, i]
            adjacent_nums.append(temp)
            adjacent_nums_idx.append(temp_idx)
    for j in range(len(adjacent_nums)):
        if int(adjacent_nums[j][0]) > int(adjacent_nums[j][1]):
            s_list[adjacent_nums_idx[j][0]] = adjacent_nums[j][1]
            s_list[adjacent_nums_idx[j][1]] = adjacent_nums[j][0]
            break
    return "".join(s_list)

print(getSmallestString("45320"))
print(getSmallestString("001"))