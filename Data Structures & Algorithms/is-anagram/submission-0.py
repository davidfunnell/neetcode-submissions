class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for index in range(len(s)):
            sDict[s[index]] = 1 + sDict.get(s[index], 0)
            tDict[t[index]] = 1 + tDict.get(t[index], 0)
        
        return sDict == tDict
