# Leet Code Algo 700. Search in a Binary Search Tree

def helperTraversal(root, val):
    if not root:
        return None
    elif root.val == val:
        return root
    if root.val > val:
        return helperTraversal(root.left, val)
    else:
        return helperTraversal(root.right, val)

def searchBST(root, val):
    return helperTraversal(root, val)