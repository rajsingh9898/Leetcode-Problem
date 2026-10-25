class Solution:
    __slots__ = ()
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m <= 2 or n <= 2:
            return 0
        def sink(start_r: int, start_c: int) -> None:
            stack = [(start_r, start_c)]
            grid[start_r][start_c] = 1
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))
        for r in range(m):
            if grid[r][0] == 0:
                sink(r, 0)
            if grid[r][n - 1] == 0:
                sink(r, n - 1)
        for c in range(n):
            if grid[0][c] == 0:
                sink(0, c)
            if grid[m - 1][c] == 0:
                sink(m - 1, c)
        closed_islands = 0
        for r in range(1, m - 1):
            row = grid[r]
            for c in range(1, n - 1):
                if row[c] == 0:
                    closed_islands += 1
                    sink(r, c)
        return closed_islands