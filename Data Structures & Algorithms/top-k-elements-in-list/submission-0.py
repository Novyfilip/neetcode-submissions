class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import numpy as np
        # my goal is to create a dictionary of letter counts
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1

        #take the keys out into a list
        keys = list(dictionary.keys())
        #sort the list
        keys.sort(key= lambda x: dictionary[x], reverse=True)

        #return list sliced by k
        return keys[:k]


        