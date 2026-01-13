# Leet Code Algo 2696. Minimum String Length After Removing Substrings

def minLength(s):
    s_arr = list(s)
    len_s = len(s)
    idx = 1
    elements_removed = 0 
    while idx + elements_removed < len_s:
        if s_arr[idx-1] + s_arr[idx] == "AB" or s_arr[idx-1] + s_arr[idx] == "CD":
            s_arr.pop(idx)
            s_arr.pop(idx-1)
            elements_removed += 2
            idx = 1
        else:
            idx += 1
    return len(s_arr)

print(minLength("ABFCACDB"))
print(minLength("ACBBD"))
print(minLength("CCCCDDDD"))
print(minLength("CCCACCACCCAAACDBBBDDDBDDBDDDBIAABA"))