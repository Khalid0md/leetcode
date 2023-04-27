import random
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        #backtracking

        subset = []
        def dfs(i):
            print(i)
            if i>= len(nums):
                res.append(subset.copy())
                print('result ' + str(res))
                return
            #decision to include nums of i
            subset.append(nums[i])
            print('subset: ' + str(subset))
            dfs(i+1)

            #decision not to include nums of i
            subset.pop()
            dfs(i+1)
        dfs(0)

        return res

    subsets(subsets, [1,2,3])