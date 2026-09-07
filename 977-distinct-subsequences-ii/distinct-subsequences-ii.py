class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        ends_with = [0] * 26
        total = 0
        for ch in s:
            idx = ord(ch) - 97
            new_count = (total + 1) % MOD
            diff = (new_count - ends_with[idx]) % MOD
            total = (total + diff) % MOD
            ends_with[idx] = new_count
        return total