# Leet Code Algo 3263. Conver Doubly Linked List To Array I

def toArray(root):
    answer = []
    if root is None:
        return answer
    currNode = root    
    while currNode:
        answer.append(currNode.val)
        currNode = currNode.next
    return answer
