# Leet Code Algo 1612. Check if Two Expression Trees are Equivalent

def helperTraversal(root, hash_map):
        if not root:
            return None
        if root.val.isalpha():
            if root.val not in hash_map:
                hash_map[root.val] = 1
            else:
                hash_map[root.val] += 1

        helperTraversal(root.left, hash_map)
        helperTraversal(root.right, hash_map)
    
def checkEquivalence(root1, root2):
    hash_one = {}
    hash_two = {}

    helperTraversal(root1, hash_one)
    helperTraversal(root2, hash_two)

    for key, value in hash_one.items():
        if key not in hash_two:
            return False
        if value != hash_two[key]:
            return False
        del hash_two[key]
    
    for key, value in hash_two.items():
        if key not in hash_one:
            return False
        if value != hash_one[key]:
            return False
    return True