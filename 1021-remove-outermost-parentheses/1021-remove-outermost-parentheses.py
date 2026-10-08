class Solution:
    __slots__ = ()
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        append = res.append
        d = 0
        for c in s:
            if c == '(':
                if d:
                    append('(')
                d += 1
            else:
                d -= 1
                if d:
                    append(')')
        return "".join(res)