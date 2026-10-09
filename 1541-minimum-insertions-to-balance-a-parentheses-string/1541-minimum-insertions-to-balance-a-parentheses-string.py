class Solution:
    __slots__ = ()
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "]")
        ans = s.count(")")
        s = s.replace(")", "]")
        parts = [len(p) for p in s.split('(')]
        it = iter(parts)
        ans += next(it)
        bal = 0
        for k in it:
            bal += 1
            if k > bal:
                ans += k - bal
                bal = 0
            else:
                bal -= k
        return ans + bal * 2