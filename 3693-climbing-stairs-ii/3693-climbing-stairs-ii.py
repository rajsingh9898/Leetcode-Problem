class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        d0, d1, d2 = float('inf'), float('inf'), 0
        for i in range(1, n + 1):
            curr = min(d2 + 1, d1 + 4, d0 + 9) + costs[i - 1]
            d0, d1, d2 = d1, d2, curr
        return d2