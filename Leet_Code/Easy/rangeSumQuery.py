# Leet Code Algo 303. Range Sum Query - Immutable

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        
    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])
    
obj1 = NumArray([-2,0,3,-5,2,-1])

print(obj1.sumRange(0,2))
print(obj1.sumRange(2,5))
print(obj1.sumRange(0,5))