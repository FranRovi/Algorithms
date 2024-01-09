# Leet Code Algo 2236. Root Equals Sum of Children

def rootEqualsSumOfChildren(root):
    if root.right.val + root.left.val == root.val:
        return True
    return False