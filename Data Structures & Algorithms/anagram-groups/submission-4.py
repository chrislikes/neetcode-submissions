class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            alp = [0]*26
            for char in word:
                alp[ord(char) - ord('a')] += 1
            if(tuple(alp) in dict):
                dict[tuple(alp)].append(word)
            else:
                dict[tuple(alp)] = [word]

        return list(dict.values())




        
        