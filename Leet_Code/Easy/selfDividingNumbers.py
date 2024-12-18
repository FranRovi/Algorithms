# Leet Code Algo 728. Self Dividing Numbers

def selfDividingNumbers(left, right):
    answer = []
    isSelfDividing = True
    for i in range(left, right + 1):
        tempStr = str(i)
        idx = 0
        while idx < (len(tempStr)):
            if int(tempStr[idx]) == 0 or i % int(tempStr[idx]) != 0:
                isSelfDividing = False
                break
            elif i % int(tempStr[idx]) == 0:               
                idx += 1
        if isSelfDividing:
            answer.append(i)
        idx = 0
        isSelfDividing = True
    return answer

print(selfDividingNumbers(1,22))
print(selfDividingNumbers(47,85))