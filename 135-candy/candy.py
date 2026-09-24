class Solution:
    def candy(self, ratings: list[int]) -> int:
        if not ratings:
            return 0
        it = iter(ratings)
        prev = next(it)
        ans = 1
        up = down = peak = 0
        for curr in it:
            if curr > prev:
                up += 1
                peak = up
                down = 0
                ans += 1 + up
            elif curr == prev:
                up = down = peak = 0
                ans += 1
            else:
                up = 0
                down += 1
                ans += down + (1 if down > peak else 0)
            prev = curr
        return ans