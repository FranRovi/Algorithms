"""
Given an array of nums and an integer target, return indeces of the two
numbers such that they  add up to the target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.

Example 1:
Input nums = [2, 7, 11, 15], target = 9:
Output: [0, 1]
Example 2:
Input nums = [3, 2, 4], target = 6:
Output: [1, 2]
Example 3:
Input nums = [3, 3], target = 6:
Output: [0, 1]
"""

def twoSums(nums, target):
    answer = []
    j = 1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)
            else:
                j += 1
        i += 1
    return answer

# print(twoSums([2, 7, 11, 15], 9))   
        
def testTwoSums():
    print(twoSums([2, 7, 11, 15], 9))
    print(twoSums([3, 2, 4], 6))
    print(twoSums([3, 3], 6))
    print(twoSums([3, 2, 3], 6))
    
def main():
    testTwoSums()


if __name__ == "__main__":
    main()


"""

   for i in range(0, len(nums) -1):
            for j in range (i+1, len(nums)-1):
                if nums[i] + nums[j] == target:
                    return [i,j]
                j += 1
            i += 1
"""