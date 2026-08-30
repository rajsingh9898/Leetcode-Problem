class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        return min(j + 1, n - i, (i + 1) + (n - j))