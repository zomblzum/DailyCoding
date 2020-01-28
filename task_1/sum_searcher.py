def list_contain_equal_sum(array, result):
    """Find sum in array function

    Checks the array for two elements whose sum is equal to the result
    """
    hash_array = {}

    for i in array:
        if hash_array.get(i) and i + i == result:
            return True 

        hash_array[result - i] = i

        if hash_array.get(i) and hash_array.get(i) != i:
            return True
