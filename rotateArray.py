def rotate(array, k):
    k = k % len(array)

    # l, r = 0, len(array) - 1
    # while l < r:
    #     array[l], array[r] = array[r], array[l]
    #     l += 1
    #     r -= 1
    
    # l, r = 0, k - 1
    # while l < r:
    #     array[l], array[r] = array[r], array[l]
    #     l += 1
    #     r -= 1

    # l, r = k, len(array) - 1
    # while l < r:
    #     array[l], array[r] = array[r], array[l]
    #     l += 1
    #     r -= 1
    
    # return array
    nums = [0] * len(array) 
    for i in range(len(array)):
        index = (i+k)%len(array)
        print(index)
        nums[index] = array[i]
        print(nums)
    
    return nums


print(rotate([1,2,3,4,5], 2))