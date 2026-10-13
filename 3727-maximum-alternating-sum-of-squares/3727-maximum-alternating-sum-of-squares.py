from itertools import islice
class Solution:
    __slots__ = ()
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sq = [x * x for x in nums]
        sq.sort()
        m = len(nums) >> 1
        return sum(sq) - 2 * sum(islice(sq, m))