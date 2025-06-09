def isMajorityElement(nums, target):
    if len(nums) == 1 and nums[0] == target:
        return True
    else:
        False 
    hash_freq_nums = {
        target:0
    }
    for num in nums:
        if num not in hash_freq_nums:
            hash_freq_nums[num] = 1
        else:
            hash_freq_nums[num] += 1
    if hash_freq_nums[target] > int(len(nums) / 2):
        return True
    else:
        return False

print(isMajorityElement([2,4,5,5,5,5,5,6,6],5))
print(isMajorityElement([10,100,101,101],101))
print(isMajorityElement([438885258],786460391))
  