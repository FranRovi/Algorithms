# Leet Code Algo 1313. Decompress Run-Length Encoded List

def decompressRunLengthEncodedList(nums):
    decompressArr = []
    for i in range(0, len(nums) - 1, 2):
        j = 0
        while j < nums[i]:
            decompressArr.append(nums[i+1])
            j += 1
    return decompressArr

print(decompressRunLengthEncodedList([1,2,3,4]))
print(decompressRunLengthEncodedList([1,1,2,3])) 