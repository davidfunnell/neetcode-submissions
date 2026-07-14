class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        length = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] not in used:
                used.add(s[r])
                r += 1
            else:
                while l < r and s[r] in used:
                    used.remove(s[l])
                    l += 1
            
            length = max(length, (r-l))        
        return length