# Leet Code Algo 3063. Linked List Frequency

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def frequencyOfElements(head):
    if head == None:
            return []
    ptr = head
    hash_frequency = {}
    while ptr != None:
        if ptr.val not in hash_frequency:
            hash_frequency[ptr.val] = 1
        else:
            hash_frequency[ptr.val] += 1
        ptr = ptr.next
    isEmpty = True    
    for key, value in hash_frequency.items():
        if isEmpty:
            new_tail = ListNode(value)
            new_head = new_tail
            isEmpty = False
        else:
            temp = ListNode(value)
            new_tail.next = temp
            new_tail = temp
    return new_head 

    # Alternative Version

    # freq_arr = list(hash_frequency.values())
    # new_tail = ListNode(freq_arr[0])
    # new_head = new_tail

    # for i in range(1, len(freq_arr)):
    #     temp = ListNode(freq_arr[i])
    #     new_tail.next = temp
    #     new_tail = temp
    # return new_head 
    