class Solution:
    __slots__ = ()
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = 0
        count = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                count += 1
        return list(range(less, less + count))