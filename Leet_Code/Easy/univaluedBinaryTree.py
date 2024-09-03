# Leet Code Algo 965. Univalued Binary Tree

def helperTraversal(root, answer):
    if not root:
        return None
    helperTraversal(root.left, answer)
    answer.add(root.val)
    helperTraversal(root.right, answer)

def isUnivalTree(root):
    answer = set()
    helperTraversal(root, answer)
    if len(answer) > 1:
        return False
    return True


