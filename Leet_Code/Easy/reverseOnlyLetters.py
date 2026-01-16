# Leet Code Algo 917. Reverse Only Letters

def reverseOnlyLetters(s):
    letter_arr = []
    len_s = len(s)
    answer = [0] * len_s
    for i in range(len_s):
        if not s[i].isalpha():
            answer[i] = s[i]
        else:
            letter_arr.append(s[i])
    right_ptr = len(letter_arr) -1
    for k in range(len_s):
        if answer[k] == 0:
            answer[k] = letter_arr[right_ptr]
            right_ptr -= 1
    return "".join(answer)

print(reverseOnlyLetters("ab-cd"))
print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))