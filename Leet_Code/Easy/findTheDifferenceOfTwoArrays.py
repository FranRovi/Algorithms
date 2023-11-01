# Leet Code Algo 2215. Find the Difference of Two Arrays

def findTheDifferenceOfTwoArrays(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    commonEle = set1.intersection(set2)
    if len(commonEle) == 1:
        commonEle = commonEle.pop()
  
        set1.remove(commonEle)
        set2.remove(commonEle)
        return [list(set1), list(set2)]
    else:
        for i in range(len(commonEle)):
            elementToDelete = commonEle.pop()
            set1.remove(elementToDelete)
            set2.remove(elementToDelete)
        return [list(set1), list(set2)]
            
    
    # print(type(set1), type(set2))
    # print(set1, set2)
    

print(findTheDifferenceOfTwoArrays([1,2,3],[2,4,6]))
print(findTheDifferenceOfTwoArrays([1,2,3,3],[1,1,2,2]))