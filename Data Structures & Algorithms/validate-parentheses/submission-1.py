class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = []
        for char in s:
            if char == "(":
                closing_brackets.append(")")
            elif char == "{":
                closing_brackets.append("}")
            elif char == "[":
                closing_brackets.append("]")
            else:
                if len(closing_brackets) == 0:
                    return False
                correct_bracket = closing_brackets.pop()
                if char != correct_bracket:
                    return False
        if len(closing_brackets) > 0:
            return False
        return True
        