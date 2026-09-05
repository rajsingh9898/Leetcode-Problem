from itertools import accumulate
class Solution:
    def smallestStableIndex(self, nums: list[int], k: int) -> int:
        suf_min = list(accumulate(reversed(nums), min))[::-1]
        pref_max = nums[0]
        for i, (x, s_min) in enumerate(zip(nums, suf_min)):
            if x > pref_max:
                pref_max = x
            if pref_max - s_min <= k:
                return i
        return -1
    firstStableIndex = smallestStableIndex