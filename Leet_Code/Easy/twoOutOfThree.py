# Leet Code Algo 2032. Two Out Of Three

def twoOutOfThree(nums1, nums2, nums3):
    answer = []
    numsHashFreq = {}
    nums1Unique = list(set(nums1))
    nums2Unique = list(set(nums2))
    nums3Unique = list(set(nums3))
    for i in range(len(nums1Unique)):
        if nums1Unique[i] not in numsHashFreq:
            numsHashFreq[nums1Unique[i]] = 1
        else:
            numsHashFreq[nums1Unique[i]] += 1
    for j in range(len(nums2Unique)):
        if nums2Unique[j] not in numsHashFreq:
            numsHashFreq[nums2Unique[j]] = 1
        else:
            numsHashFreq[nums2Unique[j]] += 1
    for k in range(len(nums3Unique)):
        if nums3Unique[k] not in numsHashFreq:
            numsHashFreq[nums3Unique[k]] = 1
        else:
            numsHashFreq[nums3Unique[k]] += 1
    # print(numsHashFreq)
    for key, value in numsHashFreq.items():
        if value > 1:
            answer.append(key)     
    return answer

print(twoOutOfThree([1,1,3,2],[2,3],[3]))
print(twoOutOfThree([3,1],[2,3],[1,2]))
print(twoOutOfThree([1,2,2],[4,3,3],[5]))