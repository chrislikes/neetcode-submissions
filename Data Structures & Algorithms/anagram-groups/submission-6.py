class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for words in strs:
            sortedWords = "".join(sorted(words))
            if(sortedWords in dict):
                dict[sortedWords].append(words)
            else:
                dict[sortedWords] = [words]
        return list(dict.values())




        
        