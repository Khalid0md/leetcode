import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #array that has as many items as nums but they are all the product of every item in num
        answer = [0] * len(nums)
        for i, x in enumerate(nums):
            #remove from array, numpy.prod it, add it back to array
            nums[i] = 1
            answer[i] = math.prod(nums)
            nums[i] = x
        return answer
            
        #works, too slow on leetcode, can i make it faster?