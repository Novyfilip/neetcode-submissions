class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #could check for the other number in a set
        numSet = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in numSet:#i check if the other half exists as an option
                return [numSet[difference],index]#if it does, 
            numSet[number] = index 

        