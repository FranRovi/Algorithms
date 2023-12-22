# Leet Code Algo 2149 Rearrange Array Elements by Sign

def rearrangeArrayElementsBySign(nums):
    positive = []
    negative = []
    arrangedArr = []
    
    for i in range(len(nums)):
        if nums[i] > 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])
    for j in range(len(positive)):
        arrangedArr.append(positive[j])
        arrangedArr.append(negative[j])
    return arrangedArr

print(rearrangeArrayElementsBySign([3,1,-2,-5,2,-4]))
print(rearrangeArrayElementsBySign([-1,1]))