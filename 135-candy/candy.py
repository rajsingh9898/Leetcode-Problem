class Solution:
    def candy(self, ratings: list[int]) -> int:
        if not ratings:
            return 0
        total = 1
        up = down = peak = 0
        for prev, curr in zip(ratings, ratings[1:]):
            if curr > prev:
                up += 1
                peak = up
                down = 0
                total += 1 + up
            elif curr == prev:
                up = down = peak = 0
                total += 1
            else:
                up = 0
                down += 1
                total += down + (1 if down > peak else 0)
        return total