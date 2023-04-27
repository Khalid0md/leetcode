class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #use a monotonic deque to add and remove and find max in O(1) time, * length of array = O(n) time
        #everything smaller than the element added is popped before so that the top of the deque is always max
        #store indices to determine if it's still in window, can always use the index to get the num
        q = collections.deque()
        res = []
        for i, cur in enumerate(nums):
            #pop smaller items at the top of the que before adding current
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)

            #remove first element if it's outside the window
            if q[0] == i - k
                q.popleft()
            # if window has k eelements add to results (first k - 1 elememts hvae < k)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

            # 8 [3 5 3] 2 5

            #abcabcbb