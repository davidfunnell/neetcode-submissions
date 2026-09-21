class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}

        for letter in magazine:
            mag_dict[letter] = mag_dict.get(letter,0) + 1

        for letter in ransomNote:
            if letter in mag_dict and mag_dict[letter] > 0:
                mag_dict[letter] -= 1
            else:
                return False
        return True