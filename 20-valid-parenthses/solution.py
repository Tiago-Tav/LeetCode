class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for c in s:
            if c == '{' or c == '(' or c == '[':
                opened.append(c)
            else:
                if opened and (opened[-1] == chr(ord(c) - 1) or opened[-1] == chr(ord(c) - 2)):
                    opened.pop()
                else:
                    return False
        if opened == []:
            return True
        else:
            return False
