def binarySearch(ordered_sequence, target):
    # mid_point = round(len(ordered_sequence) / 2)
    start = 0 
    end = len(ordered_sequence) - 1
   
    while end >= start:
        # print(mid_point)
        mid_point = round((start + end) / 2)
        if ordered_sequence[mid_point] == target:
            return "Target number found at index " + str(mid_point)
        elif ordered_sequence[mid_point] < target:
            start = mid_point + 1
        else:
            end = mid_point - 1
    return "Target number is not present in the sequence"

print(binarySearch([2, 4, 6, 8, 10, 12], 6))
print(binarySearch([1, 2, 3, 4, 5, 6], 6))
print(binarySearch([1, 3, 5, 7, 9], 8))

    


  
        