class Solution:
  def minimumChanges(self, s: str, k: int) -> int:
    n = len(s)
    divisors = [[] for _ in range(n + 1)]
    for length in range(2, n + 1):
      for d in range(1, length // 2 + 1):
        if length % d == 0:
          divisors[length].append(d)
    INF = float('inf')
    cost = [[INF] * n for _ in range(n)]
    for i in range(n):
      for j in range(i + 1, n):
        length = j - i + 1
        min_changes = INF
        for d in divisors[length]:
          changes = 0
          for rem in range(d):
            left = i + rem
            right = i + rem + ((length - 1 - rem) // d) * d
            while left < right:
              if s[left] != s[right]:
                changes += 1
              left += d
              right -= d
          if changes < min_changes:
            min_changes = changes
        cost[i][j] = min_changes
    dp = [[INF] * n for _ in range(k + 1)]
    for j in range(1, n):
      dp[1][j] = cost[0][j]
    for p in range(2, k + 1):
      for j in range(2 * p - 1, n):
        for m in range(2 * (p - 1) - 1, j - 1):
          if dp[p - 1][m] + cost[m + 1][j] < dp[p][j]:
            dp[p][j] = dp[p - 1][m] + cost[m + 1][j]
    return dp[k][n - 1]