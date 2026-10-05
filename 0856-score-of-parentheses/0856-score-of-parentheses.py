class Solution:
    __slots__ = ()
    def scoreOfParentheses(self, s: str) -> int:
        ans = d = 0
        prev = ''
        for c in s:
            if c == '(':
                d += 1
            else:
                d -= 1
                if prev == '(':
                    ans += 1 << d
            prev = c
        return ans