class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        n = len(nums)
        max_len = -1
        cur = 0
        left = 0
        for right, val in enumerate(nums):
            cur += val
            while cur > target:
                cur -= nums[left]
                left += 1
            if cur == target:
                streak = right - left + 1
                if streak > max_len:
                    max_len = streak
        return n - max_len if max_len != -1 else -1