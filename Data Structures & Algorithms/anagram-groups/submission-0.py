class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}

        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword in groupDict:
                groupDict[sortedword].append(word)
            else:
                groupDict[sortedword] = [word]
        
        return groupDict.values()