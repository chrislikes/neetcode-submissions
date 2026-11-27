class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            #[a,c,t]
            #[act]
            if(sortedWord in dict):
                dict[sortedWord].append(strs[i])
            else:
                dict[sortedWord] = [strs[i]]
        return list(dict.values())


        
        