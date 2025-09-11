# Leet Code Algo 1694. Reformat Phone Number.

def reformatNumber(number):
    nums = []
    for i in range(len(number)):
        if number[i].isdigit():
            nums.append(number[i])
    idx = 0
    len_nums = len(nums)
    answer = []
    while idx + 4 < len_nums:
        answer += nums[idx] + nums[idx+1] + nums[idx+2] + "-"
        idx += 3
    if len_nums - idx == 4:
        answer += nums[idx] + nums[idx+1] + "-" + nums[idx+2] + nums[idx+3]
    elif len_nums - idx == 3:
        answer += nums[idx] + nums[idx+1] + nums[idx+2]
    else:
        answer += nums[idx] + nums[idx+1]
    return "".join(answer)

print(reformatNumber("1-23-45 6"))
print(reformatNumber("123 4-567"))
print(reformatNumber("123 4-5678"))
    