# Leet Code Algo 1223. Maximum 69 Number

def maximum69Number(num):
    tempStr = str(num)
    tempList = list(tempStr)
    newStrNum = ''
    for i in range(len(tempList)):
        if tempList[i] == '6':
            tempList[i] = '9'
            break
    for j in range(len(tempList)):
        newStrNum += str(tempList[j])
    return int(newStrNum)

print(maximum69Number(9669))
print(maximum69Number(9969))
print(maximum69Number(9999)) 