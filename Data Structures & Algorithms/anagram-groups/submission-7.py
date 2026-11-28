class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for words in strs:
            sortedWords = "".join(sorted(words))
            if(sortedWords in hashmap):
                hashmap[sortedWords].append(words)
            else:
                hashmap[sortedWords] = [words]  
        return list(hashmap.values())             


        
        