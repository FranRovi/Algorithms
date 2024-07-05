# Leet Code Algo 2180. Count Integers With Even Digit Sum

def countEven(num):
    counter = 0
    for i in range(1, num+1):
        if i < 9:
            if i % 2 == 0:
                counter += 1
        else:
            tempStrNum = str(i)
            tempVal = 0
            for j in range(len(tempStrNum)):
                tempVal += int(tempStrNum[j])
            if tempVal % 2 == 0:
                counter += 1
    return counter

print(countEven(4))
print(countEven(30))