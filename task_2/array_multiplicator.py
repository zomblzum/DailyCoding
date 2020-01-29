import numpy as np

def multiply(array):
    result = []

    for i in range(len(array)):
        result.append(np.prod(array[:i] + array[i+1:]))

    return result