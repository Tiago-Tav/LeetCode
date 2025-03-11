class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for s in strs[1:]:
            var = ""
            total = min(len(s), len(longest))
            c = 0
            found = False
            while c < total and found == False:
                if s[c] == longest[c]:
                    var = var + s[c]
                else:
                    found = True    
                c = c + 1
            longest = var
                
        return longest