class Solution:
    __slots__ = ()
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        k = n + 2
        m = 1 << k.bit_length()
        h = m.bit_length() - 1
        shifts = list(range(h, 0, -1))
        tree_size = m << 1
        sum1 = [0] * tree_size
        sum2 = [0] * tree_size
        lazy = [0] * m
        length = [0] * tree_size
        for i in range(m):
            length[m + i] = 1
        for i in range(m - 1, 0, -1):
            length[i] = length[i << 1] << 1
        def push(p: int) -> None:
            for s in shifts:
                i = p >> s
                v = lazy[i]
                if v:
                    left = i << 1
                    right = left | 1
                    L_l = length[left]
                    s1_l = sum1[left]
                    sum2[left] = (sum2[left] + 2 * v * s1_l + v * v * L_l) % MOD
                    sum1[left] = (s1_l + v * L_l) % MOD
                    if left < m:
                        lazy[left] += v
                    L_r = length[right]
                    s1_r = sum1[right]
                    sum2[right] = (sum2[right] + 2 * v * s1_r + v * v * L_r) % MOD
                    sum1[right] = (s1_r + v * L_r) % MOD
                    if right < m:
                        lazy[right] += v
                    lazy[i] = 0
        def build(p: int) -> None:
            while p > 1:
                p >>= 1
                left = p << 1
                right = left | 1
                sum1[p] = (sum1[left] + sum1[right]) % MOD
                sum2[p] = (sum2[left] + sum2[right]) % MOD
        last = [-1] * (max(nums) + 1)
        ans = 0
        for r, x in enumerate(nums):
            ql = last[x] + 1
            qr = r
            l = ql + m
            r_idx = qr + m + 2
            push(l)
            push(r_idx)
            l_cur, r_cur = l, r_idx
            while (l_cur ^ r_cur) > 1:
                if not (l_cur & 1):
                    idx = l_cur ^ 1
                    L = length[idx]
                    s1 = sum1[idx]
                    sum2[idx] = (sum2[idx] + (s1 << 1) + L) % MOD
                    sum1[idx] = (s1 + L) % MOD
                    if idx < m:
                        lazy[idx] += 1
                if r_cur & 1:
                    idx = r_cur ^ 1
                    L = length[idx]
                    s1 = sum1[idx]
                    sum2[idx] = (sum2[idx] + (s1 << 1) + L) % MOD
                    sum1[idx] = (s1 + L) % MOD
                    if idx < m:
                        lazy[idx] += 1
                l_cur >>= 1
                r_cur >>= 1
            build(l)
            build(r_idx)
            ans = (ans + sum2[1]) % MOD
            last[x] = r
        return ans