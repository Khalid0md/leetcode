
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using this dictionary as a hashmap mapping  sorted  word to list  of matched words
        #then extracting only the values into a list
        dic = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else: 
                dic[sorted_word] += [word]
            
        return list(dic.values())
    
    def groupAnagramsNeet(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count to list of anagrams, a  default dict provides a default value for akey that is  not yet present in dict
        for x in strs:
            count=[0] * 26 # a ... z
            for c in x:
                #mapping a to 0th index using asciiv values
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(x)
            #changed above to tuple because in python dictionaries, lists cannot be keys since they are mutable
        return res.values()

    print(groupAnagrams(groupAnagrams, ["eat","tea","tan","ate","nat","bat"]))




