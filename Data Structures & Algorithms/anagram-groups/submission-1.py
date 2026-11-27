class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            alp = [0]*26
            for char in word:
                alp[ord(char) - ord('a')] += 1
            if(str(alp) in dict):
                dict[str(alp)].append(word)
            else:
                dict[str(alp)] = [word]

        return list(dict.values())




        
        