import sys
from typing import List
sys.setrecursionlimit(200000)
class Solution:
  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
      adj[parent[i]].append(i)
    last_seen = {}
    new_parent = list(parent)
    def dfs_find_parents(u: int):
      char = s[u]
      prev_ancestor = last_seen.get(char)
      if prev_ancestor is not None:
        new_parent[u] = prev_ancestor
      last_seen[char] = u
      for v in adj[u]:
        dfs_find_parents(v)
      if prev_ancestor is None:
        del last_seen[char]
      else:
        last_seen[char] = prev_ancestor
    dfs_find_parents(0)
    new_adj = [[] for _ in range(n)]
    for i in range(1, n):
      new_adj[new_parent[i]].append(i)
    answer = [1] * n
    def dfs_subtree_size(u: int) -> int:
      size = 1
      for v in new_adj[u]:
        size += dfs_subtree_size(v)
      answer[u] = size
      return size
    dfs_subtree_size(0)
    return answer