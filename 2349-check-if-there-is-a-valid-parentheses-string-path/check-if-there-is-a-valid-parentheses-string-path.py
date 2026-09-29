class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        dp = [0] * n
        dp[0] = 2
        row0 = grid[0]
        for c in range(1, n):
            dp[c] = (dp[c - 1] << 1) if row0[c] == '(' else (dp[c - 1] >> 1)
        for r in range(1, m):
            row = grid[r]
            dp[0] = (dp[0] << 1) if row[0] == '(' else (dp[0] >> 1)
            for c in range(1, n):
                mask = dp[c] | dp[c - 1]
                dp[c] = (mask << 1) if row[c] == '(' else (mask >> 1)
            if not any(dp):
                return False
        return bool(dp[-1] & 1)