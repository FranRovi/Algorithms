# Leet Code Algo 872. Leaf-Similar Trees.

def helperTraversal(root, answer):
    if not root:
        return None
    if root.left is None and root.right is None:
        answer.append(root.val)
    helperTraversal(root.left, answer)
    helperTraversal(root.right, answer)
        

def leafSimilar(root1, root2):
    tree1 = []
    tree2 = []
    helperTraversal(root1, tree1)
    helperTraversal(root2, tree2)
    len_tree1 = len(tree1)
    if len_tree1 != len(tree2):
        return False
    for i in range(len_tree1):
        if tree1[i] != tree2[i]:
            return False
    return True        