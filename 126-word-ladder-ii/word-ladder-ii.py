from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        unvisited = set(wordList)
        if endWord not in unvisited:
            return []
        unvisited.discard(beginWord)
        L = len(beginWord)
        buckets = defaultdict(list)
        for w in unvisited:
            for i in range(L):
                buckets[w[:i] + '*' + w[i + 1:]].append(w)
        parents = defaultdict(list)
        layer = {beginWord}
        found = False
        while layer and not found:
            unvisited -= layer
            next_layer = set()
            for w in layer:
                for i in range(L):
                    pat = w[:i] + '*' + w[i + 1:]
                    for nxt in buckets[pat]:
                        if nxt in unvisited:
                            parents[nxt].append(w)
                            next_layer.add(nxt)
                            if nxt == endWord:
                                found = True
            layer = next_layer
        if not found:
            return []
        res = []
        path = [endWord]
        def dfs(u: str) -> None:
            if u == beginWord:
                res.append(path[::-1])
                return
            for p in parents[u]:
                path.append(p)
                dfs(p)
                path.pop()
        dfs(endWord)
        return res