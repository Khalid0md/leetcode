import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #array that has as many items as nums but they are all the product of every item in num
        answer = [1] * len(nums)
        # for i, x in enumerate(nums):
        #     #remove from array, numpy.prod it, add it back to array
        #     nums[i] = 1
        #     answer[i] = math.prod(nums)
        #     nums[i] = x
        # return answer
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
            
        #works, too slow on leetcode, can i make it faster?
    print(productExceptSelf(productExceptSelf, [1, 2, 3, 4]))