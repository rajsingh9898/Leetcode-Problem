class Solution:
    __slots__ = ()
    def removeOuterParentheses(self, s: str) -> str:
        d = 0
        return "".join(
            [c for c in s if ((d := d + 1) > 1 if c == '(' else (d := d - 1) > 0)]
        )