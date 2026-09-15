class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = 0
        i = k - 1
        while i < n:
            start_k = i - k + 1
            if start_k >= last_end and s[start_k] == s[i]:
                sub = s[start_k : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i + 1
                    i += k
                    continue
            start_k1 = i - k
            if start_k1 >= last_end and s[start_k1] == s[i]:
                sub = s[start_k1 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i + 1
                    i += k
                    continue
            i += 1
        return ans