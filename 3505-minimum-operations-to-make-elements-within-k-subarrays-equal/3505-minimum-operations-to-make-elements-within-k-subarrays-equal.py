class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (size + 1)
    def add(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & (-idx)
        return res
    def find_kth(self, k: int) -> int:
        idx = 0
        mask = 1 << (self.n.bit_length() - 1)
        while mask > 0:
            next_idx = idx + mask
            if next_idx <= self.n and self.tree[next_idx] < k:
                idx = next_idx
                k -= self.tree[idx]
            mask >>= 1
        return idx + 1
class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        unique_vals = sorted(list(set(nums)))
        val_to_rank = {v: i + 1 for i, v in enumerate(unique_vals)}
        m = len(unique_vals)
        bit_cnt = FenwickTree(m)
        bit_sum = FenwickTree(m)
        cost = [0] * (n + 1)
        half = (x + 1) // 2
        def add_val(val: int):
            r = val_to_rank[val]
            bit_cnt.add(r, 1)
            bit_sum.add(r, val)
        def remove_val(val: int):
            r = val_to_rank[val]
            bit_cnt.add(r, -1)
            bit_sum.add(r, -val)
        def get_median_cost() -> int:
            med_rank = bit_cnt.find_kth(half)
            med_val = unique_vals[med_rank - 1]
            cnt_left = bit_cnt.query(med_rank)
            sum_left = bit_sum.query(med_rank)
            cnt_right = x - cnt_left
            total_sum = bit_sum.query(m)
            sum_right = total_sum - sum_left
            return (cnt_left * med_val - sum_left) + (
                sum_right - cnt_right * med_val
            )
        for i in range(x):
            add_val(nums[i])
        cost[x] = get_median_cost()
        for i in range(x, n):
            add_val(nums[i])
            remove_val(nums[i - x])
            cost[i + 1] = get_median_cost()
        INF = float("inf")
        dp = [0] * (n + 1)

        for j in range(1, k + 1):
            next_dp = [INF] * (n + 1)
            min_val = INF
            for i in range(j * x, n + 1):
                cand = dp[i - x] + cost[i]
                if cand < min_val:
                    min_val = cand
                if next_dp[i - 1] < min_val:
                    min_val = next_dp[i - 1]
                next_dp[i] = min_val
            dp = next_dp

        return dp[n]