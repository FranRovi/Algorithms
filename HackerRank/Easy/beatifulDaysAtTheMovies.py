# Hacker Rank Algo Beautiful Days at the Movies

def beautifulDayAtMoives(i,j,k):
    counter = 0
    for n in range(i, j+1):
        strI = str(n)
        reverseStrI = ""
        for m in range(len(strI) -1, -1, -1):
            if (m == len(strI) and strI[m] == "0"):
                continue
            else:
                reverseStrI += strI[m]
        reverseNum = int(reverseStrI)
        if (n - int(reverseNum)) % k == 0:
            counter += 1
    return counter
    
    
    strI = str(i)
    # print(strI)
    reverseStrI = ""
    # print(len(strI))
    for m in range(len(strI) -1, -1, -1):
        # print(strI[i])
        if (i == len(strI) and strI[m] == "0"):
            continue
        else:
            reverseStrI += strI[m]
    reverseNum = int(reverseStrI)
    for n in range(i, j+1):
        print(n - int(reverseNum))
        if (n - int(reverseNum)) % k == 0:
            counter += 1
    return counter
    
    
    print(reverseNum)
    
    # pass

print(beautifulDayAtMoives(20, 23, 6))