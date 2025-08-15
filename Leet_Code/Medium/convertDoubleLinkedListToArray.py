# Leet Code Algo 3294. Convert Doubly Linked List To Array II

def toArray(node):
    right_side_arr = []
    left_side_arr = []
    right_ptr = node
    while right_ptr is not None:
        right_side_arr.append(right_ptr.val)
        right_ptr = right_ptr.next
    left_ptr = node
    while left_ptr is not None:
        left_side_arr.append(left_ptr.val)
        left_ptr = left_ptr.prev
    answer = []
    for i in range(len(left_side_arr)-1,-1,-1):
        answer.append(left_side_arr[i])
    for j in range(1, len(right_side_arr)):
        answer.append(right_side_arr[j])
    return answer

