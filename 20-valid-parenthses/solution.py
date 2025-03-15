class Solution:
    def isValid(self, s: str) -> bool:
        equivalent = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for char in s:
            if char in equivalent:
                if not stack:
                    return False
                if equivalent[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
