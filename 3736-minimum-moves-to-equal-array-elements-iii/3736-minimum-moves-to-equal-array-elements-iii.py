class Solution:
    def minMoves(self, nums: list[int]) -> int:
        s = 0
        mx = nums[0]
        for x in nums:
            s += x
            if x > mx:
                mx = x
        return len(nums) * mx - s