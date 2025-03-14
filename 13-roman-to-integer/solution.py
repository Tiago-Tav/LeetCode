class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        if len(s) == 1:
            return romanNum[s]

        numList = [romanNum[s[0]]] * len(s)
        firstNum = numList[0]
        for i in range(1,len(s)):
            numList[i] = romanNum[s[i]]
            if numList[i] > numList[i - 1]:
                numList[i-1] -= numList[i-1] * 2

        return sum(numList)
            