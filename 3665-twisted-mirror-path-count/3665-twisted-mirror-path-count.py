class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        memo = {}
        def get_destination(r, c, d):
            state = (r, c, d)
            if state in memo:
                return memo[state]
            curr_r, curr_c, curr_d = r, c, d
            while True:
                if curr_d == 0:
                    curr_r += 1
                else:
                    curr_c += 1
                if not (0 <= curr_r < m and 0 <= curr_c < n):
                    memo[state] = None
                    return None
                if grid[curr_r][curr_c] == 0:
                    memo[state] = (curr_r, curr_c)
                    return (curr_r, curr_c)
                curr_d ^= 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                cnt = dp[r][c]
                if cnt == 0 or grid[r][c] == 1:
                    continue
                if c + 1 < n:
                    if grid[r][c + 1] == 0:
                        dp[r][c + 1] = (dp[r][c + 1] + cnt) % MOD
                    else:
                        dest = get_destination(r, c + 1, 0)
                        if dest:
                            nr, nc = dest
                            dp[nr][nc] = (dp[nr][nc] + cnt) % MOD
                if r + 1 < m:
                    if grid[r + 1][c] == 0:
                        dp[r + 1][c] = (dp[r + 1][c] + cnt) % MOD
                    else:
                        dest = get_destination(r + 1, c, 1)
                        if dest:
                            nr, nc = dest
                            dp[nr][nc] = (dp[nr][nc] + cnt) % MOD
        return dp[m - 1][n - 1]