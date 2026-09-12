from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        indexed = sorted(
            ((intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)),
            key=lambda x: (x[1], x[0], x[3])
        )
        end_times = [iv[1] for iv in indexed]
        INF_STATE = (1, ())
        dp = [[INF_STATE] * n for _ in range(5)]
        for i in range(n):
            l, r, w, orig_id = indexed[i]
            p = bisect_left(end_times, l) - 1
            for c in range(1, 5):
                cand = INF_STATE
                if c == 1:
                    cand = (-w, (orig_id,))
                elif p >= 0 and dp[c - 1][p] != INF_STATE:
                    prev_w_neg, prev_idx = dp[c - 1][p]
                    cand = (prev_w_neg - w, tuple(sorted(prev_idx + (orig_id,))))
                opt1 = dp[c][i - 1] if i > 0 else INF_STATE
                dp[c][i] = min(cand, opt1)
        best = min(dp[c][n - 1] for c in range(1, 5))
        return list(best[1])