# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they up to target.
# You may assume that each input would have exactly one solution, and may not
# use the element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Ouput: [0,1]
# Explanation: Becaise nums[0] + nums[1] == 9, we return[0, 1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Ouput: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Ouput: [0,1]

def twoSums(nums, target):
    answer = []
    for i in range(len(nums)- 1):
        for j in range(i +1, len(nums)):
            if nums[i] + nums[j] == target:
              answer.append(i)
              answer.append(j)
            else:
                j += 1
        else:
            i += 1
    return answer

print(twoSums([2, 7, 11, 15], 9))
print(twoSums([3,2,4], 6))
print(twoSums([3,3], 6))

 