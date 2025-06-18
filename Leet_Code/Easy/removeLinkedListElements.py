# Leet Code Algo 203. Remove Linked List Elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    new_head = ListNode()
    prev = new_head
    prev.next = head

    current = head
    while current is not None:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return new_head.next

    

