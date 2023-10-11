def find_smallest(unordered_list):
    smallest = unordered_list[0]
    smallest_index = 0
    
    for i in range(1, len(unordered_list)):
        if unordered_list[i] < smallest:
            smallest = unordered_list[i]
            smallest_index = i
    return smallest_index


def selection_sort(unordered_list):
    new_arr = []
    for i in range(len(unordered_list)):
        smallest = find_smallest(unordered_list)
        new_arr.append(unordered_list.pop(smallest))
    return new_arr

