class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strDict = {}

        for word in strs:
            charList = [0] * 26
            for char in word:
                charList[ord(char) - 97] += 1

            if tuple(charList) in strDict:
                strDict[tuple(charList)].append(word)
            else:
                strDict[tuple(charList)] = [word]
        

        result = []

        for strlist in strDict.values():
            result.append(strlist)
        return result


        