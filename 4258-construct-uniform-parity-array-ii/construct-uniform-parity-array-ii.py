class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) & 1:
            return True
        for x in nums1:
            if x & 1:
                return False
        return True
    constructUniformParityArray = uniformArray