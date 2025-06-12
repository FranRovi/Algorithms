# Leet Code Algo 234. Palindrome Linked List

def isPalindrome(head):
    nums = []
    pointer = head
    while pointer is not None:
        nums.append(pointer.val)
        pointer = pointer.next
    len_nums = len(nums)
    for i in range(len(nums) // 2):
        if nums[i] != nums[len_nums-1-i]:
            return False
    return False