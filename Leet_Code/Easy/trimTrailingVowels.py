# Leet Code Algo 3856. Trim Trailing Vowels

def trimTrailingsVowels(s):
    vowels = {"a","e","i","o","u"}
    s_list = list(s)
    for i in range(len(s_list)-1,-1,-1):
        if s_list[i] in vowels:
            s_list.pop(i)
        else:
            break
    return "".join(s_list)

print(trimTrailingsVowels("idea"))
print(trimTrailingsVowels("day"))
print(trimTrailingsVowels("aeiou"))