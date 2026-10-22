class Solution:
    __slots__ = ()
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        v = nums[0]
        is_type1 = True
        for i, x in enumerate(nums):
            if x != (v + i) % n:
                is_type1 = False
                break
        is_type2 = True
        for i, x in enumerate(nums):
            if x != (v - i) % n:
                is_type2 = False
                break
        if not is_type1 and not is_type2:
            return -1
        ans = float('inf')
        if is_type1:
            p = (n - v) % n
            ans = min(ans, p)
            if p > 0:
                ans = min(ans, n - p + 2)
        if is_type2:
            p = v
            ans = min(ans, n - p, ((p + 1) % n) + 1)
        return ans
    def minimumOperations(self, nums: list[int]) -> int:
        return self.minOperations(nums)