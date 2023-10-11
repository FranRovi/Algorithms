def quicksort(unordered_list):
    if len(unordered_list) < 2:
        return unordered_list
    else:
        pivot = unordered_list[0]
        less = [i for i in unordered_list[1:] if i <= pivot]
        
        greater = [i for i in unordered_list[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)