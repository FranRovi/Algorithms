# Leet Code Algo 404. Sum of Left Leaves

def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if root.left is None and root.right is None:
        return 0
    totalSum = []
    isRightChild = False
    self.sumHelper(root, totalSum, isRightChild)
    return sum(totalSum)

def sumHelper(self, root, totalSum, isRightChild):
    if not root:
        return None  
    if isRightChild and root.left is not None:
        isRightChild = False
    if root.left is None and root.right is None and isRightChild == False:
        totalSum.append(root.val)
    self.sumHelper(root.left, totalSum, isRightChild)
    isRightChild = True
    self.sumHelper(root.right, totalSum, isRightChild)
    isRightChild = False
    return
