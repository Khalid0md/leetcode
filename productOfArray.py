import math
def productOfArray(array):
    for i in range(len(array)):
        array[i] = math.prod(array[:i:])
    return array

print(productOfArray([1, 2, 3, 4]))