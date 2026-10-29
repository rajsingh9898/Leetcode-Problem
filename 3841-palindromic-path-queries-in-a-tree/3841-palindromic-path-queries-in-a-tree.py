import sys
sys.setrecursionlimit(200000)
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)
    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] ^= val
            idx += idx & (-idx)
    def query(self, idx):
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & (-idx)
        return res
class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOGN = 17
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        parent = [0] * n
        chars = list(s)

        from collections import deque

        q = deque([0])
        parent[0] = 0
        depth[0] = 0
        visited = [False] * n
        visited[0] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        for u in range(n):
            up[u][0] = parent[u]
        for j in range(1, LOGN):
            for u in range(n):
                up[u][j] = up[up[u][j - 1]][j - 1]
        tin = [0] * n
        tout = [0] * n
        base_mask = [0] * n
        visited_edge = [0] * n
        dfs_stack = [0]
        base_mask[0] = 1 << (ord(chars[0]) - ord("a"))
        time = 1
        tin[0] = 1
        while dfs_stack:
            u = dfs_stack[-1]
            if visited_edge[u] < len(adj[u]):
                v = adj[u][visited_edge[u]]
                visited_edge[u] += 1
                if v != parent[u]:
                    base_mask[v] = base_mask[u] ^ (
                        1 << (ord(chars[v]) - ord("a"))
                    )
                    time += 1
                    tin[v] = time
                    dfs_stack.append(v)
            else:
                tout[u] = time
                dfs_stack.pop()
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOGN):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOGN - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
        bit = FenwickTree(n)
        def get_current_mask(u):
            return base_mask[u] ^ bit.query(tin[u])
        answer = []
        for q_str in queries:
            parts = q_str.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                old_c = chars[u]
                if old_c != new_c:
                    delta = (1 << (ord(old_c) - ord("a"))) ^ (
                        1 << (ord(new_c) - ord("a"))
                    )
                    chars[u] = new_c
                    bit.update(tin[u], delta)
                    bit.update(tout[u] + 1, delta)
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = get_lca(u, v)
                mask_u = get_current_mask(u)
                mask_v = get_current_mask(v)
                char_w_mask = 1 << (ord(chars[w]) - ord("a"))
                path_mask = mask_u ^ mask_v ^ char_w_mask
                can_rearrange = (path_mask == 0) or (
                    (path_mask & (path_mask - 1)) == 0
                )
                answer.append(can_rearrange)
        return answer