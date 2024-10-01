# Leet Code Algo 3270. Find The Key of the Numbers.

def generateKey(num1, num2, num3):
    strNum1 = str(num1)
    strNum2 = str(num2)
    strNum3 = str(num3)

    answer = ""

    if len(strNum1) < 4:
        for i in range(len(strNum1),4):
            strNum1 = "0" + strNum1
    if len(strNum2) < 4:
        for j in range(len(strNum2),4):
            strNum2 = "0" + strNum2
    if len(strNum3) < 4:
        for k in range(len(strNum3),4):
            strNum3 = "0" + strNum3
    print(strNum1, strNum2, strNum3)
    for n in range(len(strNum1)):
        answer += str(min(int(strNum1[n]), int(strNum2[n]), int(strNum3[n])))
    return int(answer)

print(generateKey(1, 10, 1000))
print(generateKey(987, 879, 798))

