# Leet Code Algo 2130. Maximum Twin Sum of a Linked List 

def maximumTwinSumOfALinkedList(head):
    itr = head
    counter = 1
    maxTwinSum = -1
    arrLList = []
    while itr.next != None:
        arrLList.append(itr.val)
        itr = itr.next
        counter += 1
    arrLList.append(itr.val)
    for i in range(int(counter/2)):
        tempSum = arrLList[i] + arrLList[len(arrLList) -1 - i]
        if tempSum > maxTwinSum:
            maxTwinSum = tempSum   
    return maxTwinSum