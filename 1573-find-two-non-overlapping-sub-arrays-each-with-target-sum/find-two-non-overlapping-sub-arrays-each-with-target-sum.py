class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = 10**9
        min_len = [INF] * n
        l = 0
        cur_sum = 0
        ans = INF
        for r in range(n):
            cur_sum += arr[r]
            while cur_sum > target:
                cur_sum -= arr[l]
                l += 1
            if cur_sum == target:
                length = r - l + 1
                if l > 0 and min_len[l - 1] < INF:
                    cand = min_len[l - 1] + length
                    if cand < ans:
                        ans = cand
                prev_min = min_len[r - 1] if r > 0 else INF
                min_len[r] = length if length < prev_min else prev_min
            else:
                min_len[r] = min_len[r - 1] if r > 0 else INF
        return ans if ans < INF else -1