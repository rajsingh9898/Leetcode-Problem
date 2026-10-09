class Solution:
    __slots__ = ()
    def minInsertions(self, s: str) -> int:
        ans = req = 0
        for c in s:
            if c == '(':
                if req & 1:
                    ans += 1
                    req += 1 
                else:
                    req += 2
            else:
                req -= 1
                if req < 0:
                    ans += 1
                    req = 1  
        return ans + req