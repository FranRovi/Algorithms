# Leet Code Algo 3663. Find The Least Frequent Digit

def getLeastFrequentDigit(n):
    freq_nums = {}
    str_num = str(n)
    for i in range(len(str_num)):
        if str_num[i] not in freq_nums:
            freq_nums[str_num[i]] = 1
        else:
            freq_nums[str_num[i]] += 1
    sorted_dict = dict(sorted(freq_nums.items(), key=lambda item: (item[1], item[0])))
    for key, value in sorted_dict.items():
        return int(key)
    
print(getLeastFrequentDigit(1553322))
print(getLeastFrequentDigit(723344511))