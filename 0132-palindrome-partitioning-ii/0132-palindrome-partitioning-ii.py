class Solution:
    __slots__ = ()
    def minCut(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]
        if s == s_rev:
            return 0
        for i in range(1, n):
            if s[:i] == s_rev[-i:] and s[i:] == s_rev[:n - i]:
                return 1
        dp = list(range(-1, n))
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                new_cut = dp[l] + 1
                if new_cut < dp[r + 1]:
                    dp[r + 1] = new_cut
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                new_cut = dp[l] + 1
                if new_cut < dp[r + 1]:
                    dp[r + 1] = new_cut
                l -= 1
                r += 1
        return dp[n]