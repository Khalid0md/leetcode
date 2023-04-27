from collections import Counter
class Solution:
    #return true if t is an arhument of s
    # use two hashmaps, one for each string letter -> count
    # if hashmaps are equal, anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {} # Hashmap

        for i in range(len(s)):
            #countS[s[i]] = 1 + countS.s[i] will throw a key does not exist
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

    def isAnagramOneLine(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def isAnagramSpace(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False

        S = sorted(s)
        T = sorted(t)

        return S == T


    s = 'modell'
    t = 'ledom'

    print(isAnagram(isAnagram, s, t))
    print(isAnagramOneLine(isAnagramOneLine, s, t))
    print(isAnagramSpace(isAnagramSpace, s, t))
            