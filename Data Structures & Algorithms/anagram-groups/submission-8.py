class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for words in strs: 
            count = [0]*26 
            for char in words:
                count[ord(char) - ord('a')] += 1
            count = tuple(count) 
            if(count in hashmap):
                hashmap[count].append(words)
            else:
                hashmap[count] = [words]
        return list(hashmap.values())
        