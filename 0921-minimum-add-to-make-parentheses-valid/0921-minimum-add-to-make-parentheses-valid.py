class Solution:
    __slots__ = ()
    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0
        for c in s:
            if c == '(':
                bal += 1
            elif bal:
                bal -= 1
            else:
                ans += 1
        return ans + bal