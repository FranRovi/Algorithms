# Leet Code Algo 1302. Deepest Leaves Sum


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helperTraversal(self, root, answer, level):
        if not root:
            level = -1
            return None
        
        self.helperTraversal(root.left, answer, level+1)
        if level not in answer:
            answer[level] = [root.val]
        else:
            answer[level].append(root.val)
        self.helperTraversal(root.right, answer, level+1)
        

def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    answer = {}
    level = 0
    self.helperTraversal(root, answer, level)
    sort_dict = dict(sorted(answer.items(), key=lambda item: item[0], reverse=True))
    val_leafs = list(sort_dict.values())[0]
    # return answer
    return sum(val_leafs)

