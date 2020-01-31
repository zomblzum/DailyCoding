import numpy as np

def get_positive_subarray(array):
    array = np.array(array)
    return array[array > 0]

def find_lowest_positive_missing_integer_in_array(input_array):
    array = get_positive_subarray(input_array)
    array_len = len(array)

    for i in range(array_len): 
        if (abs(array[i]) - 1 < array_len and array[abs(array[i]) - 1] > 0): 
            array[abs(array[i]) - 1] *= -1 
             
    for i in range(array_len): 
        if (array[i] > 0): 
            return i + 1

    return array_len + 1
