# Leet Code Algo 3823. Reverse Letters Then Special Characters in a String

def reverseByType(s):
    s_list = list(s)
    letters = []
    special_chars = []
    for char in s:
        if char.isalpha():
            letters.append(char)
        else:
            special_chars.append(char)
    letters_idx = len(letters) - 1
    special_idx = len(special_chars) - 1

    for i in range(len(s)):
        if s_list[i].isalpha():
            s_list[i] = letters[letters_idx]
            letters_idx -= 1
        else:
            s_list[i] = special_chars[special_idx]
            special_idx -= 1
    return "".join(s_list)

print(reverseByType(")ebc#da@f("))
print(reverseByType("z"))
print(reverseByType("!@#$%^&*()"))