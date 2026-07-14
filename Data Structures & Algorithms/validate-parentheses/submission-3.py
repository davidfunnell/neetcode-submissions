class Solution:
    def isValid(self, s: str) -> bool:
        validStack = []
        openBracket = {'}':'{', ')':'(', ']': '['}

        for char in s:
            if char in openBracket.values():
                validStack.append(char)
            else:
                if len(validStack) == 0:
                    return False

                last = validStack.pop()
                if last != openBracket[char]:
                    return False
        
        if validStack:
            return False
        else:
            return True