from math import comb
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, 2 * k) % 1_000_000_007