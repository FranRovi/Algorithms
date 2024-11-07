# Leet Code Algo 2283. Check if Number Has Equal Digit Count and Digit Value

def digitCount(num):
    hashNums = {}
    for i in range(len(num)):
        hashNums[str(i)] = 0
    print(hashNums)
    for j in range(len(num)):
        if num[j] in hashNums:
            hashNums[num[j]] += 1
    answer = ""
    for key,value in hashNums.items():
        answer += str(value)
    if answer == num:
        return True
    return False

print(digitCount("1210"))
print(digitCount("030")) 