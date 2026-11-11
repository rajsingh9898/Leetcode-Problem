class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        opt1 = need1 * cost1 + need2 * cost2
        m = min(need1, need2)
        rem1 = need1 - m
        rem2 = need2 - m
        opt2 = m * costBoth + rem1 * cost1 + rem2 * cost2
        M = max(need1, need2)
        opt3 = M * costBoth
        return min(opt1, opt2, opt3)