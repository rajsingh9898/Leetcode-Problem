class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        if k == 1:
            return [n - q[2] for q in queries]
        m = 1
        while m < n:
            m <<= 1
        tree_prod = [1] * (2 * m)
        tree_cnt = [[0] * k for _ in range(2 * m)]
        for i in range(n):
            u = m + i
            v = nums[i] % k
            tree_prod[u] = v
            tree_cnt[u][v] = 1
        for u in range(m - 1, 0, -1):
            left = 2 * u
            right = left + 1
            p_left = tree_prod[left]
            tree_prod[u] = (p_left * tree_prod[right]) % k
            c_left = tree_cnt[left]
            c_right = tree_cnt[right]
            c_u = tree_cnt[u]
            for i in range(k):
                c_u[i] = c_left[i]
            for r in range(k):
                c_u[(p_left * r) % k] += c_right[r]
        valid_r = [[[] for _ in range(k)] for _ in range(k)]
        for p in range(k):
            for r in range(k):
                rem = (p * r) % k
                valid_r[p][rem].append(r)

        ans = []
        for idx, val, start, x in queries:
            u = m + idx
            v = val % k
            tree_prod[u] = v
            c_u = tree_cnt[u]
            for i in range(k):
                c_u[i] = 0
            c_u[v] = 1
            u //= 2
            while u > 0:
                left = 2 * u
                right = left + 1
                p_left = tree_prod[left]
                tree_prod[u] = (p_left * tree_prod[right]) % k
                c_left = tree_cnt[left]
                c_right = tree_cnt[right]
                c_u = tree_cnt[u]
                for i in range(k):
                    c_u[i] = c_left[i]
                for r in range(k):
                    c_u[(p_left * r) % k] += c_right[r]
                u //= 2                
            l = start + m
            r = n - 1 + m
            right_nodes = []
            cur_prod = 1
            res = 0
            while l <= r:
                if l % 2 == 1:
                    c_node = tree_cnt[l]
                    for r_val in valid_r[cur_prod][x]:
                        res += c_node[r_val]
                    cur_prod = (cur_prod * tree_prod[l]) % k
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2
            for node in reversed(right_nodes):
                c_node = tree_cnt[node]
                for r_val in valid_r[cur_prod][x]:
                    res += c_node[r_val]
                cur_prod = (cur_prod * tree_prod[node]) % k
            ans.append(res)
        return ans
    def __getattr__(self, name):
        return self.resultArray