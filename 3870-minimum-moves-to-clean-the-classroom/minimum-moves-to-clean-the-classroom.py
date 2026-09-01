from collections import deque
class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_id = {}
        k = 0
        start_r = start_c = 0
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'L':
                    litter_id[(r, c)] = k
                    k += 1
                elif ch == 'S':
                    start_r, start_c = r, c
        target_mask = (1 << k) - 1
        if target_mask == 0:
            return 0
        total_states = m * n * (1 << k)
        max_energy = bytearray(total_states)
        q = deque([(start_r, start_c, 0, energy, 0)])
        start_idx = ((start_r * n + start_c) << k)
        max_energy[start_idx] = energy + 1
        popleft = q.popleft
        append = q.append
        while q:
            r, c, mask, cur_e, dist = popleft()
            next_dist = dist + 1 
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    ch = classroom[nr][nc]
                    if ch == 'X':
                        continue 
                    ne = cur_e - 1
                    nmask = mask 
                    if ch == 'L' and (nr, nc) in litter_id:
                        nmask |= (1 << litter_id[(nr, nc)]) 
                    if nmask == target_mask:
                        return next_dist 
                    if ch == 'R':
                        ne = energy
                    elif ne == 0:
                        continue
                    idx = ((nr * n + nc) << k) | nmask
                    if ne + 1 <= max_energy[idx]:
                        continue
                    max_energy[idx] = ne + 1
                    append((nr, nc, nmask, ne, next_dist))   
        return -1
    minimumMoves = minMoves