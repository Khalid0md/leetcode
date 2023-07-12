from collections import Counter
import heapq
class Solution:
    def isNStraightHand(hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        #use hashmap to count number of cards for each value
        hashmap = Counter(hand)
        hmap = {}
        for n in hand:
            hmap[n] = 1 + hmap.get(n, 0)
        print(hashmap)
        print(hmap)

        minH = list(hashmap.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            
            for i in range(first, first + groupSize):
                if i not in hashmap:
                    return False
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
                        

        #be greedy, always look for minimum vals to start groups with, if we can do that group, great, if not, return false
        # to get min value avaliable, iterate through hashmap in O(n), or use a minheap to keep track of min available
        #popping from minheap somehting which is not the minimum is impossible
        #but if we get to that point, we already lost


    
    isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
