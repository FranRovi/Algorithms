# Hacker Rank Algo. Modified Kaprekar Numbers

def modifiedKaprekarNums(p, q):
    answer = []
    for i in range(p, q+1):
        if i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000:
            continue
        tempNum = i ** 2
        tempNumStr = str(tempNum)
        numLeftStr = ""
        numRightStr = ""
        if len(tempNumStr) % 2 == 0:
            midVal = int(len(tempNumStr) / 2)
            for j in range(midVal):
                numLeftStr += tempNumStr[j]
                numRightStr += tempNumStr[j + midVal]
            if int(numLeftStr) + int(numRightStr) == i:
                answer.append(i)
        else:
            if i == 1:
                answer.append(i)
            else:
                if (i != 1 and len(tempNumStr) == 1):
                    continue
                midVal = int(len(tempNumStr) / 2)
                for k in range(midVal):
                    
                    numLeftStr += tempNumStr[k]
                    numRightStr += tempNumStr[k + 1 + midVal]
                
                leftAlternative = numLeftStr + tempNumStr[midVal]
                rightAlternative = f"{tempNumStr[midVal]}{numRightStr}"

                allZeros = set(numRightStr)
                allZerosRightAlt = set(rightAlternative)
                
                if (len(numRightStr) > 1 and numRightStr[0] == "0"):
                    numRightStr = numRightStr[1:]
                if (len(numRightStr) > 1 and len(allZeros) == 1):
                    numRightStr = "0"
        
                if (len(rightAlternative) > 1 and rightAlternative[0] == "0"):
                    rightAlternative = rightAlternative[1:]
                if (len(rightAlternative) > 1 and len(allZerosRightAlt) == 1):
                    rightAlternative = "0"

                if (int(leftAlternative) + int(numRightStr) == i or int(numLeftStr) + int(rightAlternative) == i):
                    answer.append(i)
            
    if len(answer) > 0:
        print(*answer, sep=' ')
    else:
        print('INVALID RANGE')

modifiedKaprekarNums(1, 100)
modifiedKaprekarNums(100, 300)