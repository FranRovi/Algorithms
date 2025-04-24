# Leet Code Algo 1265. Print Linked List in reverse

def printLinkedListInReverse(head):
    arr = []
    ptr = head
    while ptr != None:
        arr.append(ptr)
        ptr = ptr.getNext()
    for i in range(len(arr)-1,-1,-1):
        print(arr[i].printValue())