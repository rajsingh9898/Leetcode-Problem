class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, x in enumerate(nums):
            digit_sum = 0
            val = x
            while val > 0:
                digit_sum += val % 10
                val //= 10
            if digit_sum == i:
                return i
        return -1