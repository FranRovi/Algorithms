# Add Leet Code Algo 530. Minimum Absolute Difference in BST
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helperTraversal(self, root, nums):
    if not root:
        return None
    self.helperTraversal(root.left, nums)
    nums.append(root.val)
    self.helperTraversal(root.right, nums)
 
def getMinimumDifference(self, root):
    nums = []
    self.helperTraversal(root, nums)
    min_diff = 100000
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] < min_diff:
            min_diff = nums[i] - nums[i-1]
        if min_diff == 1:
            break
    return min_diff 