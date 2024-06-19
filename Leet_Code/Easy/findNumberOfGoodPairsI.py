# Leet Code Algo 3162. Find the Number of Good Pairs I

def numberOfPairs(nums1, nums2, k):
    counter = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                counter +=1
    return counter

print(numberOfPairs([1,3,4],[1,3,4],1))
print(numberOfPairs([1,2,4,12],[2,4],3))  
      