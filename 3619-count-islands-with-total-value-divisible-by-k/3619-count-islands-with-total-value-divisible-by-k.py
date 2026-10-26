class Solution:
    __slots__ = ()
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        valid_islands = 0
        for r in range(m):
            row = grid[r]
            for c in range(n):
                if row[c] <= 0:
                    continue
                island_sum = row[c]
                row[c] = 0
                stack = [(r, c)]
                pop = stack.pop
                append = stack.append
                while stack:
                    cr, cc = pop()
                    if cr > 0 and grid[cr - 1][cc] > 0:
                        island_sum += grid[cr - 1][cc]
                        grid[cr - 1][cc] = 0
                        append((cr - 1, cc))
                    if cr + 1 < m and grid[cr + 1][cc] > 0:
                        island_sum += grid[cr + 1][cc]
                        grid[cr + 1][cc] = 0
                        append((cr + 1, cc))
                    if cc > 0 and grid[cr][cc - 1] > 0:
                        island_sum += grid[cr][cc - 1]
                        grid[cr][cc - 1] = 0
                        append((cr, cc - 1))
                    if cc + 1 < n and grid[cr][cc + 1] > 0:
                        island_sum += grid[cr][cc + 1]
                        grid[cr][cc + 1] = 0
                        append((cr, cc + 1))
                if island_sum % k == 0:
                    valid_islands += 1
        return valid_islands
    count_islands = countIslands