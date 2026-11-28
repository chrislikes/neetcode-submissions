class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        listA = []
        
        for nums in nums:
            if(nums in hashmap):
                hashmap[nums] += 1

            else:
                hashmap[nums] = 1
        for i in range(k):
            #retrieve the highest value 
            highest_key = max(hashmap, key=hashmap.get)
             #check if array empty so do a append or = and add to array
            if(listA != None):
                listA.append(highest_key)
            hashmap.pop(highest_key)
            #afterwards remove highest value from hashmap
        return listA

        #O(N^2) time complexitity

        