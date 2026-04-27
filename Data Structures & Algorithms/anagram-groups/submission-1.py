class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this part builds dictionary
        groups = {}
        for word in strs:
           key = tuple(sorted(word))#anagrams ahve the same key
           if key not in groups:
                groups[key] = []
           groups[key].append(word)
        return list(groups.values())

                



        