class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, b in enumerate(s.encode(), 1):
            total += i * (123 - b)
        return total