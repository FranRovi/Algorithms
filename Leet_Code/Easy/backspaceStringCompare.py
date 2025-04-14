# Leet Code Algo 844. Backspace String Compare

def backspaceCompare(s, t):
    answer_s = []
    for i in range(len(s)):
        if s[i] == "#":
            if len(answer_s) == 0:
                continue
            else:
                answer_s.pop()
        else:
            answer_s.append(s[i])
    answer_t = []
    for j in range(len(t)):
        if t[j] == "#":
            if len(answer_t) == 0:
                continue
            else:
                answer_t.pop()
        else:
            answer_t.append(t[j])
    if answer_s == answer_t:
        return True
    return False

print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))
