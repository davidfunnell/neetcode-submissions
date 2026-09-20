class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        left = math.inf
        right = math.inf
        result = math.inf

        for i, word in enumerate(wordsDict):
            if word == word1:
                left = i
            elif word == word2:
                right = i
            
            result = min(result, abs(right - left))
        
        return result