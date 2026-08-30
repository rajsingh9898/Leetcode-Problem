class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        if i > j:
            i, j = j, i
        return min(j + 1, n - i, i + 1 + n - j)