# Leet Code Algo 876. Middle of the Linked List

class ListNode:
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node
        
def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

list_odd = ListNode(1)
list_odd.next = ListNode(2)
list_odd.next.next = ListNode(3)
list_odd.next.next.next = ListNode(4)
list_odd.next.next.next.next = ListNode(5)

list_even = ListNode(1)
list_even.next = ListNode(2)
list_even.next.next = ListNode(3)
list_even.next.next.next = ListNode(4)
list_even.next.next.next.next = ListNode(5)
list_even.next.next.next.next.next = ListNode(6)

print(middleNode(list_odd))
print(middleNode(list_even))