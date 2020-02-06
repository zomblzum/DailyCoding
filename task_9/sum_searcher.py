def find_max_sum_of_non_adjacent(array):
    previous, largest = 0, 0
    
    for item in array:
        previous, largest = largest, max(largest, previous + item)

    return largest