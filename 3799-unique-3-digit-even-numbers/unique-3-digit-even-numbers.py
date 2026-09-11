from itertools import permutations
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        return len({
            a * 100 + b * 10 + c
            for a, b, c in permutations(digits, 3)
            if a != 0 and not (c & 1)
        })
    unique3DigitEvenNumbers = totalNumbers