class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        present = set(nums)
        multiple = k
        while multiple in present:
            multiple += k
        return multiple