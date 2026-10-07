class Solution:
    __slots__ = ()
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []
        append = ans.append
        def dfs(s: str, last_i: int, last_j: int, open_ch: str, close_ch: str) -> None:
            count = 0
            n = len(s)
            for i in range(last_i, n):
                c = s[i]
                if c == open_ch:
                    count += 1
                elif c == close_ch:
                    count -= 1
                if count < 0:
                    for j in range(last_j, i + 1):
                        if s[j] == close_ch and (j == last_j or s[j] != s[j - 1]):
                            dfs(s[:j] + s[j + 1:], i, j, open_ch, close_ch)
                    return
            rev = s[::-1]
            if open_ch == '(':
                dfs(rev, 0, 0, ')', '(')
            else:
                append(rev)
        dfs(s, 0, 0, '(', ')')
        return ans