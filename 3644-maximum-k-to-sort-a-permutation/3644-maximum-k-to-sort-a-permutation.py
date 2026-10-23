class Solution:
    __slots__ = ()
    def maxK(self, nums: list[int]) -> int:
        if nums[0] != 0:
            return 0
        ans = -1
        for i, x in enumerate(nums):
            if x != i:
                ans &= (x & i)
                if not ans:
                    return 0
        return 0 if ans == -1 else ans
    maximumK = maxK
    findMaxK = maxK
    maxSortableK = maxK
    sortPermutation = maxK