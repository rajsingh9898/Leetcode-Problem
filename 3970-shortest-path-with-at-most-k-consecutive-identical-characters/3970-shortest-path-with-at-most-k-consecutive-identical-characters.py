import heapq
class Solution:
    def shortestPath(
        self, n: int, edges: list[list[int]], labels: str, k: int
    ) -> int:
        if k < 1:
            return -1
        if n == 1:
            return 0
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        stride = k + 1
        INF = float("inf")
        dist = [INF] * (n * stride)
        start_state = 0 * stride + 1
        dist[start_state] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, count = heapq.heappop(pq)
            if d > dist[u * stride + count]:
                continue
            if u == n - 1:
                return d
            u_label = labels[u]
            for v, w in adj[u]:
                next_count = count + 1 if labels[v] == u_label else 1
                if next_count <= k:
                    next_state = v * stride + next_count
                    if d + w < dist[next_state]:
                        dist[next_state] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))
        return -1