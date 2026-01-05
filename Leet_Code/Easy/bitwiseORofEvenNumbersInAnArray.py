# Leet Code Algo 3688. Bitwise OR of Even Numbers in an Array

def evenNumberBitwiseORs(nums):
    even_nums_arr = []
    for n in nums:
        if n % 2 == 0:
            even_nums_arr.append(n)
    answer = 0
    for i in range(len(even_nums_arr)):
        answer |= even_nums_arr[i]
    return answer

print(evenNumberBitwiseORs([1,2,3,4,5,6]))
print(evenNumberBitwiseORs([7,9,11]))
print(evenNumberBitwiseORs([1,8,16]))