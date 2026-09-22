class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        result = 0

        sDict = {}
        for char in s:
            sDict[char] = 1 + sDict.get(char, 0)
        
        for value in sDict.values():
            if value % 2 > 0:
                result += 1
            if result > 1:
                return False

        return True