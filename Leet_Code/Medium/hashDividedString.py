# Leet Code Algo 3271. Hash Divided String

def stringHash(s, k):
    hash_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8,
                        "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
                        "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
        
    hash_nums = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i",
                    9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r",
                    18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}
    answer = ""
    idx = 0
    while idx < len(s):
        temp_str =  s[idx: idx+k]
        temp_sum = 0
        for i in range(len(temp_str)):
            temp_sum += hash_letters[temp_str[i]]
        answer += hash_nums[temp_sum % 26]
        temp_sum = 0
        idx += k
    return answer

print(stringHash("abcd", 2))
print(stringHash("mxz", 3))
print(stringHash("y", 1))