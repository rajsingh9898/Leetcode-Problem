class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cur = 0
        for c in s:
            if c == '(':
                cur += 1
                if cur > ans:
                    ans = cur
            elif c == ')':
                cur -= 1
        return ans