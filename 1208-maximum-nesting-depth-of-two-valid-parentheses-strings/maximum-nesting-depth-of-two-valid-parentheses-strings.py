class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                ans.append(d & 1)
                d += 1
            else:
                d -= 1
                ans.append(d & 1)
        return ans