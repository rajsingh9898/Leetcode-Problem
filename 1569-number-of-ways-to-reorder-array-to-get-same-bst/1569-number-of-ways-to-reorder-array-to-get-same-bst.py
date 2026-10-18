import sys
sys.setrecursionlimit(2000)
MOD = 1_000_000_007
MAX_N = 1005
FACT = [1] * MAX_N
INV = [1] * MAX_N
for i in range(1, MAX_N):
    FACT[i] = (FACT[i - 1] * i) % MOD
INV[MAX_N - 1] = pow(FACT[MAX_N - 1], MOD - 2, MOD)
for i in range(MAX_N - 2, -1, -1):
    INV[i] = (INV[i + 1] * (i + 1)) % MOD
class Solution:
    __slots__ = ()
    def numOfWays(self, nums: list[int]) -> int:
        fact = FACT
        inv = INV
        def dfs(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            l_len = len(left)
            r_len = len(right)
            ways = (fact[l_len + r_len] * inv[l_len] % MOD * inv[r_len]) % MOD
            return (ways * dfs(left) % MOD * dfs(right)) % MOD
        return (dfs(nums) - 1) % MOD