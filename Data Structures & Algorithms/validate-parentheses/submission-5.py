class Solution:
    def isValid(self, s: str) -> bool:
        response = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []

        for item in s:
            if item not in response:
                stack.append(item)
            else:
                if stack and stack[-1] == response[item]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
