class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        result = 0

        for word in words:
            result += 1
            setWord = set(word)

            for char in setWord:
                if char not in allowed:
                    result -= 1
                    break
        
        return result
            