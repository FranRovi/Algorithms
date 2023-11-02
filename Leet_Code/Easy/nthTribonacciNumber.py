# Leet Code 1137. N-th Tribonacci Number

def nthTribonacciNumber(n):
    answer = 0
    if n <= 3:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return 2
    else: 
        tribonacciArr = [0, 1, 1]
        for i in range(2, n-1):
            # print()
            print(i ,tribonacciArr[i-2] + tribonacciArr[i-1] + tribonacciArr[i])
            tribonacciArr.append(tribonacciArr[i-2] + tribonacciArr[i-1] + tribonacciArr[i])
            answer = tribonacciArr[-3] + tribonacciArr[-2] + tribonacciArr[-1]
    return answer 
print(nthTribonacciNumber(3))
# print(nthTribonacciNumber(4))
# print(nthTribonacciNumber(25))
        