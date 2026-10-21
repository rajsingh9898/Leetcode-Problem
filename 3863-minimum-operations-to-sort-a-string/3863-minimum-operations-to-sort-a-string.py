class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        min_char = min(s)
        max_char = max(s)
        if s[0] == min_char or s[-1] == max_char:
            return 1
        if s.find(min_char) < n - 1 or s.rfind(max_char) > 0:
            return 2
        return 3