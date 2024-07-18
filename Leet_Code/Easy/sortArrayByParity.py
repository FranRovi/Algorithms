# Leet Code Algo 905. Sort Array By Parity

def sortArrayByParity(nums):
    evenArr = []
    oddArr = []
    answer = []
    if nums == [0]:
        return [0]
    for num in nums:
        if num % 2 == 0:
            evenArr.append(num)
        else:
            oddArr.append(num)
    for j in range(len(evenArr)):
        answer.append(evenArr[j])
    for k in range(len(oddArr)):
        answer.append(oddArr[k])
    return answer

print(sortArrayByParity([3,1,2,4]))
print(sortArrayByParity([0]))
    