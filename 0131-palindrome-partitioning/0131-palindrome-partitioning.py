class Solution:
    __slots__ = ()
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s]]
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j + 1]
                if sub == sub[::-1]:
                    adj[i].append((j + 1, sub))
        res = []
        path = []
        append_path = path.append
        pop_path = path.pop
        append_res = res.append
        def dfs(u: int) -> None:
            if u == n:
                append_res(path.copy())
                return
            for v, sub in adj[u]:
                append_path(sub)
                dfs(v)
                pop_path()
        dfs(0)
        return res