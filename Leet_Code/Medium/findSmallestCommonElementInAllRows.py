# Leet Code Algo 1198. Find Smallest Common Element in All Rows

def smallestCommonElement(mat):
    hash_nums = {}
    n = len(mat)
    m = len(mat[0])
    highest_num = mat[0][-1]
    for i in range(m):
        hash_nums[mat[0][i]] = 1
    for j in range(1, n):
        for k in range(m):
            if mat[j][k] in hash_nums:
                hash_nums[mat[j][k]] += 1
            elif mat[j][k] > highest_num:
                break
    for key, value in hash_nums.items():
        if value == n:
            return key
    return -1

print(smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))
print(smallestCommonElement([[1,2,3],[2,3,4],[2,3,5]]))  