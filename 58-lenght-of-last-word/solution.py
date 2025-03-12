ECHO est  ativado.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        solution = ''
        change = False
        s = ' ' + s
        for c in s[::-1]:
            if c == ' ' and change == True:
                return len(solution)
            else:
                if not c == ' ':
                    change = True
                    solution = solution + c

                    
        
        