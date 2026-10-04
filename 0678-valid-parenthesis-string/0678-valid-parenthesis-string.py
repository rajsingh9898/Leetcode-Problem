class Solution:
    __slots__ = ()
    def checkValidString(self, s: str) -> bool:
        if s[0] == ')' or s[-1] == '(':
            return False
        cmin = cmax = 0
        for ch in s:
            if ch == '(':
                cmin += 1
                cmax += 1
            elif ch == ')':
                cmin = cmin - 1 if cmin > 0 else 0
                cmax -= 1
                if cmax < 0:
                    return False
            else:
                cmin = cmin - 1 if cmin > 0 else 0
                cmax += 1
        return cmin == 0