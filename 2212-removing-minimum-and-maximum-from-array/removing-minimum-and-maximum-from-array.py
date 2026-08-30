class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        if i > j:
            i, j = j, i
        left = j + 1
        right = n - i
        both = i + 1 + n - j
        ans = left if left < right else right
        return ans if ans < both else both