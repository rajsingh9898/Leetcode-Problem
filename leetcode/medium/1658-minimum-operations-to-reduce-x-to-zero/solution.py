class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        left = 0
        cur = 0
        while left < n and cur + nums[left] <= x:
            cur += nums[left]
            left += 1
        min_ops = left if cur == x else float('inf')
        left -= 1
        right = n - 1
        while right >= 0:
            cur += nums[right]
            while left >= 0 and (cur > x or left >= right):
                cur -= nums[left]
                left -= 1
            if cur == x:
                ops = (left + 1) + (n - right)
                if ops < min_ops:
                    min_ops = ops
            if left < 0 and cur >= x:
                break
            right -= 1
        return min_ops if min_ops != float('inf') else -1