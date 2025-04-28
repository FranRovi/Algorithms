# Leet Code Algo 760. Find Anagram Mappings

def anagramMappings(nums1, nums2):
    answer = []
    hash_nums_2 = {}
    for i in range(len(nums2)):
        hash_nums_2[nums2[i]] = i
    for j in range(len(nums1)):
        answer.append(hash_nums_2[nums1[j]])
    return answer

print(anagramMappings([12,28,46,32,50],[50,12,32,46,28]))
print(anagramMappings([84,46],[84,46]))