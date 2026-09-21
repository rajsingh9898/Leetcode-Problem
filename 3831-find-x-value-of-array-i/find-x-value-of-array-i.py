class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        total = n * (n + 1) // 2
        if k == 1:
            return [total]
        if k == 2:
            dp1 = ans1 = 0
            for x in nums:
                if x % 2:
                    dp1 += 1
                else:
                    dp1 = 0
                ans1 += dp1
            return [total - ans1, ans1]
        if k == 3:
            dp1 = dp2 = 0
            ans1 = ans2 = 0
            for x in nums:
                v = x % 3
                if v == 1:
                    dp1 += 1
                elif v == 2:
                    dp1, dp2 = dp2, dp1 + 1
                else:
                    dp1 = dp2 = 0
                ans1 += dp1
                ans2 += dp2
            return [total - ans1 - ans2, ans1, ans2]
        if k == 4:
            dp1 = dp2 = dp3 = 0
            ans1 = ans2 = ans3 = 0
            for x in nums:
                v = x % 4
                if v == 1:
                    dp1 += 1
                elif v == 3:
                    dp1, dp3 = dp3, dp1 + 1
                elif v == 2:
                    dp1, dp2, dp3 = 0, dp1 + dp3 + 1, 0
                else:
                    dp1 = dp2 = dp3 = 0
                ans1 += dp1
                ans2 += dp2
                ans3 += dp3
            return [total - ans1 - ans2 - ans3, ans1, ans2, ans3]
        dp1 = dp2 = dp3 = dp4 = 0
        ans1 = ans2 = ans3 = ans4 = 0
        for x in nums:
            v = x % 5
            if v == 1:
                dp1 += 1
            elif v == 2:
                dp1, dp2, dp3, dp4 = dp3, dp1 + 1, dp4, dp2
            elif v == 3:
                dp1, dp2, dp3, dp4 = dp2, dp4, dp1 + 1, dp3
            elif v == 4:
                dp1, dp2, dp3, dp4 = dp4, dp3, dp2, dp1 + 1
            else:
                dp1 = dp2 = dp3 = dp4 = 0
            ans1 += dp1
            ans2 += dp2
            ans3 += dp3
            ans4 += dp4
        return [total - ans1 - ans2 - ans3 - ans4, ans1, ans2, ans3, ans4]