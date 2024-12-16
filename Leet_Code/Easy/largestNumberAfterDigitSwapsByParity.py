# Leet Code Algo 2231. Largest Number After Digit Swaps by Parity

def largestInteger(num):
    arrIdxEven = []
    arrIdxOdd = []
    answerArrParity = []
    strNum = str(num)
    if len(strNum) == 1:
        return num
    for num in strNum:
        if int(num) % 2 == 0:
            arrIdxEven.append(int(num))
            answerArrParity.append("E")
        else:
            arrIdxOdd.append(int(num))
            answerArrParity.append("O")   
    sortedArrIdxEven = sorted(arrIdxEven, reverse = True)
    sortedArrIdxOdd = sorted(arrIdxOdd, reverse = True)
    evenPtr = 0
    oddPtr = 0
    idx = 0
    answerArr = []
    while idx < len(sortedArrIdxEven) + len(sortedArrIdxOdd):
        if answerArrParity[idx] == "E":
            answerArr.append(sortedArrIdxEven[evenPtr])
            evenPtr += 1
        else:
            answerArr.append(sortedArrIdxOdd[oddPtr])
            oddPtr += 1
        idx += 1
    answer = ""
    for num in answerArr:
        answer += str(num)
    return int(answer)

print(largestInteger(1234))
print(largestInteger(65875))