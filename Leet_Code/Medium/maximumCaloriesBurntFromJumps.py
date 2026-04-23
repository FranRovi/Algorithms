# Leet Code Algo 3730. Maximum Calories Burnt From Jumps

def maxCaloriesBurnt(heights):
    sorted_heights = sorted(heights)
    len_heights = len(heights)
    left_ptr = 0
    right_ptr = len_heights - 1
    idx = 0
    prev = 0
    total_count = 0
    while idx < len_heights:
        if idx % 2 == 0:
            total_count += abs(prev - sorted_heights[right_ptr]) ** 2
            prev = sorted_heights[right_ptr]
            right_ptr -= 1
        else:
            total_count += abs(prev - sorted_heights[left_ptr]) ** 2
            prev = sorted_heights[left_ptr]
            left_ptr += 1
        idx += 1
    return total_count

print(maxCaloriesBurnt([1,7,9]))
print(maxCaloriesBurnt([5,2,4]))
print(maxCaloriesBurnt([3,3]))