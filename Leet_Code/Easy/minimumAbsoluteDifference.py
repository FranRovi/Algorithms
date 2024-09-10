# Leet Code Algo 1200. Minimum Absolute Difference

def minimumAbsDifference(arr):
    minDiff = 9999
    answer = []
    sortedArr = sorted(arr)
    # print(sortedArr)
    for i in range(len(arr)-1):
        if abs(sortedArr[i] - sortedArr[i +1]) < minDiff:
            minDiff = abs(sortedArr[i] - sortedArr[i +1])
            answer = []
            answer.append([sortedArr[i], sortedArr[i+1]])
        elif abs(sortedArr[i] - sortedArr[i +1]) == minDiff:
            answer.append([sortedArr[i], sortedArr[i+1]])
    return answer
              
    # answer = []
    # hashDifference = {}
    # for i in range(len(arr) -1):
    #     for j in range(i+1, len(arr)):
    #         if abs(arr[i] - arr[j]) not in hashDifference:
    #             if arr[i] > arr[j]:
    #                 hashDifference[abs(arr[i] - arr[j])] = [[arr[j], arr[i]]]
    #             else:
    #                 hashDifference[abs(arr[i] - arr[j])] = [[arr[i], arr[j]]]
    #         else:
    #             if arr[i] > arr[j]:
    #                 hashDifference[abs(arr[i] - arr[j])].append([arr[j], arr[i]])
    #             else:
    #                 hashDifference[abs(arr[i] - arr[j])].append([arr[i], arr[j]])
    # # print(hashDifference)
    # sortedTupleDifferences = sorted(hashDifference.items(), key= lambda x:x[0])
    # sortedHashByOccurrences = dict(sortedTupleDifferences)
    # # print(sortedHashByOccurrences)
    # for key, value in sortedHashByOccurrences.items():
    #     # print("Length: " + str(len(value)))
    #     # if len(value) == 2:
    #     #     return [value]
    #     answer = value
    #     break
    # return sorted(answer)
    
# print(minimumAbsDifference([4,2,1,3]))
# print(minimumAbsDifference([1,3,6,10,15]))
# print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
# print(minimumAbsDifference([-57,-70,6,-69,5,-47,-13]))
print(minimumAbsDifference([40,11,26,27,-20]))
