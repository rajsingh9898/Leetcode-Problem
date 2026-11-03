class Solution:
    def minMoves(self, nums: list[int]) -> int:
        max_val = max(nums)
        return sum(max_val - x for x in nums)