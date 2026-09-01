class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        num_cells = m * n
        litter_mask = [0] * num_cells
        is_reset = [False] * num_cells
        start_u = 0
        k = 0
        for r in range(m):
            row = classroom[r]
            row_offset = r * n
            for c in range(n):
                ch = row[c]
                u = row_offset + c
                if ch == 'L':
                    litter_mask[u] = 1 << k
                    k += 1
                elif ch == 'S':
                    start_u = u
                elif ch == 'R':
                    is_reset[u] = True
        target_mask = (1 << k) - 1
        if target_mask == 0:
            return 0
        adj = [[] for _ in range(num_cells)]
        for r in range(m):
            row_offset = r * n
            for c in range(n):
                if classroom[r][c] == 'X':
                    continue
                u = row_offset + c
                nbrs = adj[u]
                if r > 0 and classroom[r - 1][c] != 'X':
                    nbrs.append((r - 1) * n + c)
                if r + 1 < m and classroom[r + 1][c] != 'X':
                    nbrs.append((r + 1) * n + c)
                if c > 0 and classroom[r][c - 1] != 'X':
                    nbrs.append(row_offset + c - 1)
                if c + 1 < n and classroom[r][c + 1] != 'X':
                    nbrs.append(row_offset + c + 1)
        max_e = bytearray(num_cells << k)
        max_e[start_u << k] = energy + 1
        queue = [(start_u, 0, energy)]
        dist = 0
        while queue:
            dist += 1
            next_queue = []
            for u, mask, cur_e in queue:
                ne_base = cur_e - 1
                for v in adj[u]:
                    l_bit = litter_mask[v]
                    nmask = mask | l_bit if l_bit else mask
                    if nmask == target_mask:
                        return dist
                    if is_reset[v]:
                        ne = energy
                    else:
                        if ne_base == 0:
                            continue
                        ne = ne_base
                    idx = (v << k) | nmask
                    if ne + 1 <= max_e[idx]:
                        continue
                    max_e[idx] = ne + 1
                    next_queue.append((v, nmask, ne))
            queue = next_queue
        return -1
    minimumMoves = minMoves