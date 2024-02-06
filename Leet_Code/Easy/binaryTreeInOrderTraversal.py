# Add Leet Code Algo 94. Binary Tree Inorder Traversal
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helperTraversal(self, root, answer):
    if not root:
        return None
    self.helperTraversal(root.left, answer)
    answer.append(root.val)
    self.helperTraversal(root.right, answer)
 
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    answer = []
    self.helperTraversal(root, answer)
    return answer