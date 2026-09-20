class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        ans = 0
        while s:
            if len(s) <= ans:
                break
            x = s.pop()
            l = x - 1
            while l in s:
                s.remove(l)
                l -= 1
            r = x + 1
            while r in s:
                s.remove(r)
                r += 1
            ans = max(ans, r - l - 1)
        return ans