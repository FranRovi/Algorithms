# Leet Code Algo 3794. Reverse String Prefix

def reversePrefix(s, k):
    if k == 1:
        return s
    temp = s[:k]
    reverse_temp = ""
    for i in range(len(temp)-1,-1,-1):
        reverse_temp += temp[i]
    return reverse_temp + s[k:]

print(reversePrefix("abcd", 2))
print(reversePrefix("xyz", 3))
print(reversePrefix("hey", 1))
