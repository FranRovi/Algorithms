# Leet Code Algo 2164. Sort Even and Odd Indices Independently

def sortEvenOdd(nums):
    oddArr = []
    evenArr = []
    for i in range(0, len(nums), 2):
        evenArr.append(nums[i])
    for j in range(1, len(nums), 2):
        oddArr.append(nums[j])
    oddArrSorted = sorted(oddArr, reverse = True)
    evenArrSorted = sorted(evenArr)
    answer = []
    lenSmallerArr = len(evenArrSorted) if len(evenArrSorted) <= len(oddArrSorted) else len(oddArrSorted)
    lenLargerArr = len(evenArrSorted) if len(evenArrSorted) > len(oddArrSorted) else len(oddArrSorted)
    largerArr = evenArrSorted if len(evenArrSorted) > len(oddArrSorted) else oddArrSorted
    for k in range(lenSmallerArr):
        answer.append(evenArrSorted[k])
        answer.append(oddArrSorted[k])
    for l in range(lenSmallerArr, lenLargerArr):
        answer.append(largerArr[l])
    return answer

print(sortEvenOdd([4,1,2,3]))
print(sortEvenOdd([2,1]))