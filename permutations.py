class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]] #does a deep copy
        
        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        print(result)
        return result

tmp = Solution() 
tmp.permute([1, 2, 3])
        