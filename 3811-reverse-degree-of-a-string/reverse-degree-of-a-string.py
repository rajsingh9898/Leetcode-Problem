class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, 1):
            rev_pos = ord('z') - ord(ch) + 1
            total += i * rev_pos
        return total