# Leet Code Algo 1630. Arithmetic Subarrays.

def checkArithmeticSubarrays(nums, l, r):
    answer = []
    len_l = len(l)
    for i in range(len_l):
        subarr = nums[l[i]:r[i]+1]
        sorted_subarr = sorted(subarr)
        dif = abs(sorted_subarr[0] - sorted_subarr[1])
        is_escape = False
        for j in range(1, len(subarr)-1):
            if abs(sorted_subarr[j] - sorted_subarr[j+1]) != dif:
                answer.append(False)
                is_escape = True
                break
        if is_escape == False:
            answer.append(True)
        is_escape = False
    return answer

print(checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
print(checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10])) 
    