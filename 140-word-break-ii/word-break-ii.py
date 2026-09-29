class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        if set(s) - set("".join(wordDict)):
            return []
        word_set = set(wordDict)
        max_len = max(map(len, wordDict))
        n = len(s)
        memo = {n: [""]} 
        def dfs(i: int) -> list[str]:
            if i in memo:
                return memo[i]
            res = []
            for j in range(i + 1, min(n + 1, i + max_len + 1)):
                word = s[i:j]
                if word in word_set:
                    for rest in dfs(j):
                        res.append(word + (" " + rest if rest else ""))
            memo[i] = res
            return res
        return dfs(0)