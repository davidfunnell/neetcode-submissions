class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        # print(ord("a")) == 97


        # dictionary for anagrams where key is key for anagrams and values are all anagrams
        aDict = {}

        # for loop to go though all strs

        for s in strs:
            temp = []
            for i in range(26):
                temp.append(0)
            for letter in s:
                temp[ord(letter) - 97] += 1
            
            key = tuple(temp)

            if key in aDict:
                aDict[key].append(s)
            else:
                aDict[key] = [s]       


        # return values from dictionary

        return list(aDict.values())

