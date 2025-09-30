# Leet Code Algo 3696. Maximum Distance Between Unequal Words in Array I

def max_distance(words):
    max_distance = 0
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if words[i] != words[j]:
                if j - i + 1 > max_distance:
                    max_distance = j - i + 1
    return max_distance

print(max_distance(["leetcode","leetcode","codeforces"]))
print(max_distance(["a","b","c","a","a"]))
print(max_distance(["z","z","z"]))