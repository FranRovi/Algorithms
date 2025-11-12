# Leet Code Algo 942. DI String Match

def diStringMatch(s):
    left_id = 0
    right_id = len(s)
    answer = []
    for char in s:
        if char == "D":
            answer.append(right_id)
            right_id -= 1
        else:
            answer.append(left_id)
            left_id += 1
    answer.append(left_id)
    return answer

print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDI"))

        