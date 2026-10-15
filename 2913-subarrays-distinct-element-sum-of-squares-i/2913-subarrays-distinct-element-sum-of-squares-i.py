class Solution:
    __slots__ = ()
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        last = [-1] * 101
        ans = 0
        curr_sum = 0
        for r, x in enumerate(nums):
            prev = last[x]
            diff = 0
            for l in range(prev + 1, r + 1):
                val = dp[l]
                diff += (val << 1) | 1
                dp[l] = val + 1
            curr_sum += diff
            ans += curr_sum
            last[x] = r
        return ans