# Leet Code Algo 414. Third Maximum Number

def thirdMax(nums):
    # make a new list with no duplicate nums  
    set_nums = set(nums)
    unique_nums_list = list(set_nums) 

    # sort new list
    sorted_num_arr = sorted(unique_nums_list)

    if len(sorted_num_arr) == 1:
        return sorted_num_arr[0]  
    elif len(sorted_num_arr) == 2:
        return sorted_num_arr[-1]
    else:
        return sorted_num_arr[-3]
    
print(thirdMax([3,2,1]))
print(thirdMax([1,2]))
print(thirdMax([2,2,3,1]))