class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pointer = 0
        result = 0

        keyDict = {}
        for i, letter in enumerate(keyboard):
            keyDict[letter] = i
        
        for char in word:
            result += abs(pointer - keyDict[char])
            pointer = keyDict[char]
        
        return result