from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        dq = deque()
        for l in range(n - 1, -1, -1):
            val = nums[l]
            cnt = 1
            while dq and dq[0][0] <= val:
                prev_val, prev_cnt = dq.popleft()
                cost += (val - prev_val) * prev_cnt
                cnt += prev_cnt
            dq.appendleft([val, cnt])
            while cost > k:
                cost -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans