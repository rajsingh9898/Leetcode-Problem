LOOKUP = [0] * 100000
for i in range(1, 100000):
    LOOKUP[i] = LOOKUP[i // 10] + (i % 10)
class Solution:
    __slots__ = ()
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        lookup = LOOKUP
        keys = [((lookup[x // 100000] + lookup[x % 100000]) << 30) | x for x in nums]
        order = sorted(range(n), key=keys.__getitem__)
        cycles = 0
        for i in range(n):
            if order[i] < 0:
                continue
            cycles += 1
            cur = i
            while order[cur] >= 0:
                nxt = order[cur]
                order[cur] = -1
                cur = nxt
        return n - cycles