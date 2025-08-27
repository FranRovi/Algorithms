# Hacker Rank Algo. Permuting Two Arrays.

def twoArrays(k, A, B):
    arrA_sorted = sorted(A)
    arrB_sorted = sorted(B, reverse=True)
    for i in range(len(A)):
        if arrA_sorted[i] + arrB_sorted[i] < k:
            return "NO"
    return "YES"

print(twoArrays(1,[0,1],[0,2]))
print(twoArrays(10,[2,1,3],[7,8,9]))
print(twoArrays(5,[1,2,2,1],[3,3,3,4]))
print(twoArrays(10,[7,6,8,4,2],[5,2,6,3,1]))