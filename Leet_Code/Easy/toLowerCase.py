# Leet Code 709. To Lower Case

def toLowerCase(s):
    answer = ''
    for i in range(len(s)):
        answer += s[i].lower()
    return answer

print(toLowerCase('Hello'))
print(toLowerCase('Here'))
print(toLowerCase('LOVELY'))