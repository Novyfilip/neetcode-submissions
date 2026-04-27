class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for element in nums:
            if element not in unique:
                unique.append(element)
        if nums != unique:
            return True
        else:
            return False
        