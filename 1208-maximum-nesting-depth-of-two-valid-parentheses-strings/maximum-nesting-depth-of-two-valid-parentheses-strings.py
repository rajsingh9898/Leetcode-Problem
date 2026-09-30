class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        append = ans.append
        d = 0
        for c in seq:
            if c == '(':
                d ^= 1
                append(d)
            else:
                append(d)
                d ^= 1
        return ans