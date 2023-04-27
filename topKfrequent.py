from collections import defaultdict
class Solution:
    def topKfrequent(self, nums: list[int], k: int) -> list[int]:
        #hashmap dict with numbers as keys and map to frequencies
        hashmap = defaultdict(int)
        for num  in nums:
            hashmap[num] = hashmap[num] + 1
        print(hashmap)
        #sorting a dictionary
        m = dict(sorted(hashmap.items(), key=lambda pair :  pair[1], reverse=True))
        print(m)
        l = list(m.keys())
        print(l[0:k])
        return l[0:k]
    
    topKfrequent(topKfrequent, [1,1,1,2,2,3], 2)