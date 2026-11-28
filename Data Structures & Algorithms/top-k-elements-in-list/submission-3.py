class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        listA = []
        
        for num in nums:
            if(num in hashmap):
                hashmap[num] += 1

            else:
                hashmap[num] = 1
        for i in range(k):
            #retrieve the highest value 
            highest_key = max(hashmap, key=hashmap.get)
            #do a append
            listA.append(highest_key)
            #afterwards remove highest value from hashmap
            hashmap.pop(highest_key)
        return listA

        #O(N^2) time complexitity

        