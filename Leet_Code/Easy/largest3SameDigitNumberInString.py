# Leet Code Algo 2264. Largest 3-Same-Digit Number in String

def largestGoodInteger(num):
    answer = ''
    largestVal = -1
    for i in range(2, len(num)):
        if num[i-1] == num[i] and num[i-1] == num[i-2]:
            if int(num[i]) > largestVal:
                largestVal = int(num[i])
                answer = num[i] * 3
    return answer
    
print(largestGoodInteger("6777133339"))
print(largestGoodInteger("2300019")) 
print(largestGoodInteger("42352338"))  