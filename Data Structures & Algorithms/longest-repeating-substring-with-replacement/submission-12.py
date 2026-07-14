class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0


        for index in range(len(s)):
            print(index)
            temp = k
            r = index + 1
            
            while temp >= 0 and r < len(s):
                if s[index] != s[r]:
                    temp -= 1
                if temp >= 0:
                    r += 1
                print("r:",  r)
                print("temp:", temp)
            distance = r-index
            if r == len(s) and temp > 0:
                distance = min((distance+temp), len(s))
 
            length = max(length, distance)
            print(length)
        
        return length
