class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetterCounts = {}
        tLetterCounts = {}
        for letter in s:
            sLetterCounts[letter] = sLetterCounts.get(letter, 0) + 1
        for letter in t:
            tLetterCounts[letter] = tLetterCounts.get(letter, 0) + 1
        if sLetterCounts == tLetterCounts:
            return True
        else: return False
        