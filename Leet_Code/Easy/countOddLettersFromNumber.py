# Leet Code Algo 3581. Count Odd Letters from Number

def countOddLetters(n):
    hash_nums = {
        "1":"one","2":"two","3":"three","4":"four",
        "5":"five","6":"six","7":"seven","8":"eight",
        "9":"nine","0":"zero"
    }
    temp_str = ""
    temp_num = str(n)
    for c in temp_num:
        temp_str += hash_nums[c]
    hash_freq = {}
    for i in range(len(temp_str)):
        if temp_str[i] not in hash_freq:
            hash_freq[temp_str[i]] = 1
        else:
            hash_freq[temp_str[i]] += 1
    counter = 0
    freq_arr = list(hash_freq.values())
    for j in range(len(freq_arr)):
        if freq_arr[j] % 2 != 0:
            counter += 1
    return counter

print(countOddLetters(41))
print(countOddLetters(20))