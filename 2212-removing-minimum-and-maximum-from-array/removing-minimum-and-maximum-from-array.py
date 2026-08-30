class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        if i > j:
            i, j = j, i
        ans1 = j + 1
        ans2 = n - i
        ans3 = ans1 + ans2 - n - 1 + n 
        return min(ans1, ans2, i + 1 + n - j)