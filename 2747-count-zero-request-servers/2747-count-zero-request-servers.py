from collections import defaultdict
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        ans = [0] * len(queries)
        server_freq = defaultdict(int)
        active_servers = 0
        l = 0
        r = 0
        m = len(logs)
        for orig_idx, q in sorted_queries:
            while r < m and logs[r][1] <= q:
                s_id = logs[r][0]
                if server_freq[s_id] == 0:
                    active_servers += 1
                server_freq[s_id] += 1
                r += 1
            while l < m and logs[l][1] < q - x:
                s_id = logs[l][0]
                server_freq[s_id] -= 1
                if server_freq[s_id] == 0:
                    active_servers -= 1
                l += 1
            ans[orig_idx] = n - active_servers
        return ans