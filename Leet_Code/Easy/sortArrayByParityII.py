# Leet Code Algo 922. Sort Array By Parity II

def sortArrayByParityII(nums):
    evenArr = []
    oddArr = []
    answer = []
    for num in nums:
        if num % 2 == 0:
            evenArr.append(num)
        else:
            oddArr.append(num)
    for j in range(len(evenArr)):
        answer.append(evenArr[j])
        answer.append(oddArr[j])
    return answer
    
print(sortArrayByParityII([4,2,5,7]))
print(sortArrayByParityII([2,3]))
    