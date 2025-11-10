# Leet Code Algo 350. Intersection of Two Arrays II

def intersect(nums1, nums2):
    hash_nums1 = {}
    hash_nums2 = {}

    for n in nums1:
        if n not in hash_nums1:
            hash_nums1[n] = 1
        else:
            hash_nums1[n] += 1
    for n in nums2:
        if n not in hash_nums2:
            hash_nums2[n] = 1
        else:
            hash_nums2[n] += 1

    answer = []
    shorter_dict = hash_nums1 if len(hash_nums1) <= len(hash_nums2) else hash_nums2 
    longer_dict = hash_nums1 if len(hash_nums1) > len(hash_nums2) else hash_nums2

    for key, value in shorter_dict.items():
        if key in longer_dict:
            if value == longer_dict[key]:
                for i in range(value):
                    answer.append(key)
            elif value < longer_dict[key]:
                for j in range(value):
                    answer.append(key)
            else:
                for k in range(longer_dict[key]):
                    answer.append(key)
    return answer

print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))