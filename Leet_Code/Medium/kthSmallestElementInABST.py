# Leet Code Algo 230. Kth Smallest Element in a BST

def helperTraversal(self, root, arr):
    if not root:
        return None
    arr.append(root.val)
    self.helperTraversal(root.left, arr)
    self.helperTraversal(root.right, arr)

def kthSmallest(root, k):
    values = []
    helperTraversal(root, values)
    sorted_values = sorted(values)
    return sorted_values[k-1]