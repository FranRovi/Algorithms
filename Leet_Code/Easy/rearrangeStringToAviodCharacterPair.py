# Leet Code Algo 3992. Rearrange String to Avoid Character Pair

def rearrangeString(s, x, y):
    y_counter = 0
    for i in range(len(s)):
        if s[i] == y:
            y_counter += 1
    answer = "" + y * y_counter
    for c in s:
        if c != y:
            answer += c
    return answer

print(rearrangeString("aabc", "a", "c"))
print(rearrangeString("dcab", "d", "b"))
print(rearrangeString("axe", "o", "x"))