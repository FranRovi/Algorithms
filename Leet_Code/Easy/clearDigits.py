# Leet Code Algo 3174. Clear Digits

def clearDigits(s):
    listString = list(s)
    idx = 0
    while idx < len(listString):
        if listString[idx].isdigit():
            for i in range(idx, -1, -1):
                if listString[i].isalpha():
                    del listString[idx]
                    del listString[i]
                    idx -= 2
                    break
        idx += 1
    answer = ""
    for ele in listString:
        answer += ele
    return answer

print(clearDigits("abc"))
print(clearDigits("cb34"))
