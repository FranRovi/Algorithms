# Leet Code Algo 1422. Maximum Score After Splitting a String

def maxScore(s):
    left_counter = right_counter = 0
    left_string = s[0]
    right_string = s[1:]
    if s[0] == "0":
        left_counter = 1
    for i in range(1, len(s)):
        if s[i] == "1":
            right_counter += 1
    max_score = left_counter + right_counter 
    for j in range(1, len(s)- 1):
        if s[j] == "1":
            right_counter -= 1
        else:
            left_counter += 1
        if left_counter + right_counter > max_score:
            max_score = left_counter + right_counter
    return max_score
    
print(maxScore("011101"))
print(maxScore("00111"))
print(maxScore("1111"))
print(maxScore("00"))