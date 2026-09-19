class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s, best = set(nums), 0
        for x in s:
            if x - 1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                best = max(best, y - x)
        return best