# Leet Code Algo 1305. All Elements in Two Binary Search Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def helperTraversal(root, arr):
        if not root:
            return None
        helperTraversal(root.left, arr)
        arr.append(root.val)
        helperTraversal(root.right, arr)
    
    
def getAllElements(tree1, tree2):
    tree_values = []
    helperTraversal(tree1, tree_values)
    helperTraversal(tree2, tree_values)
    return sorted(tree_values)

root_1 = TreeNode(2)
node_1_1 = TreeNode(1)
node_1_4 = TreeNode(4)

root_2 = TreeNode(1)
node_2_0 = TreeNode(0)
node_2_3 = TreeNode(3)

root_3 = TreeNode(1)
node_3_8 = TreeNode(8)

root_4 = TreeNode(8)
node_4_1 = TreeNode(1)

root_1.left = node_1_1
root_1.right = node_1_4

root_2.left = node_2_0
root_2.right = node_2_3

root_3.right = node_3_8

root_4.left = node_4_1

print(getAllElements(root_1, root_2))
print(getAllElements(root_3, root_4))
