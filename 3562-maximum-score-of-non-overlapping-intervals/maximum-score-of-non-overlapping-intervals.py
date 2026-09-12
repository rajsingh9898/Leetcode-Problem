from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        indexed = sorted(
            ((iv[0], iv[1], iv[2], i) for i, iv in enumerate(intervals)),
            key=lambda x: (x[1], x[0], x[3])
        )
        n = len(indexed)
        end_times = [iv[1] for iv in indexed]
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        for i, (l, r, w, orig_id) in enumerate(indexed):
            p = bisect_left(end_times, l)
            for c in range(1, 5):
                opt_w, opt_idx = dp[c][i]
                prev_w, prev_idx = dp[c - 1][p]
                if c > 1 and prev_w == 0:
                    dp[c][i + 1] = dp[c][i]
                    continue
                cur_w = prev_w + w
                if cur_w < opt_w:
                    dp[c][i + 1] = dp[c][i]
                elif cur_w > opt_w:
                    dp[c][i + 1] = (cur_w, tuple(sorted(prev_idx + (orig_id,))))
                else:
                    cand_idx = tuple(sorted(prev_idx + (orig_id,)))
                    if cand_idx < opt_idx:
                        dp[c][i + 1] = (cur_w, cand_idx)
                    else:
                        dp[c][i + 1] = dp[c][i]
        best_w = 0
        best_idx = ()
        for c in range(1, 5):
            w, idx = dp[c][n]
            if w > best_w:
                best_w = w
                best_idx = idx
            elif w == best_w and w > 0 and idx < best_idx:
                best_idx = idx
        return list(best_idx)