# Leet Code Algo 3456. Find Special Substring of Length K

def hasSpecialSubstring(s, k):
    len_s = len(s)
    if k == 1 and len_s == 1:
        return True
    counter = 1
    temp = [s[0]]
    for i in range(1, len_s):
        if s[i] != temp[-1]:
            if k == 1:
                return True 
            temp = [s[i]]
            counter = 1
        else:
            temp.append(s[i])
            counter += 1
            if counter == k:
                if i + 1 < len_s:
                    if s[i + 1] != temp[-1]:
                        return True
                elif i + 1 == len_s:
                    return True             
    return False

print(hasSpecialSubstring("aaabaaa", 3))
print(hasSpecialSubstring("abc", 2))
print(hasSpecialSubstring("jkjhfgg", 2))
print(hasSpecialSubstring("ccc", 2))
print(hasSpecialSubstring("h", 1))
print(hasSpecialSubstring("gckhijh", 1))
