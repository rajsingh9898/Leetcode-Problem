class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            v = num % k
            new_dp = [0] * k
            new_dp[v] += 1
            for r in range(k):
                if dp[r]:
                    new_dp[(r * v) % k] += dp[r]
            for r in range(k):
                ans[r] += new_dp[r]
            dp = new_dp
        return ans