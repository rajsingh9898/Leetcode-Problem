DIGIT_SUM = [
    (x % 10) + ((x // 10) % 10) + ((x // 100) % 10) + (x // 1000)
    for x in range(1001)
]
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(min(len(nums), 28)):
            if DIGIT_SUM[nums[i]] == i:
                return i
        return -1