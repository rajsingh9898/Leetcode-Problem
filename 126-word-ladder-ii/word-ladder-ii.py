from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        layer = {beginWord}
        words.discard(beginWord)
        parents = defaultdict(list)
        found = False
        while layer and not found:
            words -= layer
            next_layer = set()
            for word in layer:
                for i in range(len(word)):
                    p1, p2 = word[:i], word[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        cand = p1 + c + p2
                        if cand in words:
                            parents[cand].append(word)
                            next_layer.add(cand)
                            if cand == endWord:
                                found = True
            layer = next_layer
        if not found:
            return []
        res = []
        path = [endWord]
        def dfs(node: str) -> None:
            if node == beginWord:
                res.append(path[::-1])
                return
            for p in parents[node]:
                path.append(p)
                dfs(p)
                path.pop()
        dfs(endWord)
        return res