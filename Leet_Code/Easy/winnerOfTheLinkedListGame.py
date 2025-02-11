# Leet Code Algo 3062. Winner of the Linked List Game

def gameResult(head):
    ptr = head
    idx = 0
    even_arr = []
    odd_arr = []
    counter = 0
    while ptr is not None:
        if idx % 2 == 0:
            even_arr.append(ptr.val)
        else:
            odd_arr.append(ptr.val)
        idx += 1
        ptr = ptr.next
    for i in range(len(even_arr)):
        if even_arr[i] > odd_arr[i]:
            counter += 1
        elif even_arr[i] < odd_arr[i]:
            counter -= 1
    if counter > 0:
        return "Even"
    elif counter < 0:
        return "Odd" 
    else:
        return "Tie"
    