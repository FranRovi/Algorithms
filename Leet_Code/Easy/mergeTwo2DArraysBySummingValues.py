# Leet Code Algo 2570. Merge Two 2D Arrays by Summing Values

def mergeArrays(nums1, nums2):
    answer = []
    hash_nums = {}
    for i in range(len(nums1)):
        if nums1[i][0] not in hash_nums:
            hash_nums[nums1[i][0]] = nums1[i][1]
    for j in range(len(nums2)):
        if nums2[j][0] not in hash_nums:
            hash_nums[nums2[j][0]] = nums2[j][1]
        else:
                hash_nums[nums2[j][0]] += nums2[j][1]
    sorted_dict_items = sorted(hash_nums.items())
    sorted_dict_nums = dict(sorted_dict_items)
    for key, value in sorted_dict_nums.items():
        answer.append([key, value])
    return answer

print(mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))
print(mergeArrays([[2,4],[3,6],[5,5]],[[1,3],[4,3]]))