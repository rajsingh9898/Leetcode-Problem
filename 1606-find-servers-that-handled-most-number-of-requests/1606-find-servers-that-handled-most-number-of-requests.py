import heapq
class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
        for i in range(1, n + 1):
            self.add(i, 1)
    def add(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    def query(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

    def find_kth(self, k: int) -> int:
        """Find the 1-based index of the k-th available server (1 <= k <= total)."""
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
    def busiestServers(
        self, k: int, arrival: list[int], load: list[int]
    ) -> list[int]:
        bit = FenwickTree(k)
        busy = []
        count = [0] * k

        for i, (t, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, s_id = heapq.heappop(busy)
                bit.add(s_id, 1)

            total_free = bit.query(k)
            if total_free == 0:
                continue

            target_1based = (i % k) + 1
            free_before_target = bit.query(target_1based - 1)

            if total_free > free_before_target:
                chosen_server = bit.find_kth(free_before_target + 1)
            else:
                chosen_server = bit.find_kth(1)
            bit.add(chosen_server, -1)
            count[chosen_server - 1] += 1
            heapq.heappush(busy, (t + dur, chosen_server))

        max_req = max(count)
        return [i for i, c in enumerate(count) if c == max_req]