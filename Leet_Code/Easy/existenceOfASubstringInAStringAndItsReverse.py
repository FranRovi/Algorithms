# Leet Code Algo 3083. Existence of a Substring in a String and Its Reverse

def isSubstringPresent(s):
    if len(s) <= 1:
        return False
    reverse_str = ""
    for i in range(len(s)-1, -1, -1):
        reverse_str += s[i]
    temp_str = [reverse_str[0]]
    temp_str.append(reverse_str[1])
    for j in range(2, len(reverse_str)):
        if "".join(temp_str) not in s:
            temp_str.pop(0)
            temp_str.append(reverse_str[j])
        else:
            return True
    if temp_str[0] == temp_str[1]:
        return True
    return False

print(isSubstringPresent("leetcode"))
print(isSubstringPresent("abcba"))
print(isSubstringPresent("abcd"))
print(isSubstringPresent("e"))
print(isSubstringPresent("uuxqvxrlh"))