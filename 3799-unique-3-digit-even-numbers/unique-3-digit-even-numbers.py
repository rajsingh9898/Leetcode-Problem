class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1
        evens = [d for d in (0, 2, 4, 6, 8) if cnt[d]]
        if not evens:
            return 0
        avail = [d for d in range(10) if cnt[d]]
        ans = 0
        for d1 in avail:
            if d1 == 0:
                continue
            cnt[d1] -= 1
            for d2 in avail:
                if not cnt[d2]:
                    continue
                cnt[d2] -= 1
                for d3 in evens:
                    if cnt[d3]:
                        ans += 1
                cnt[d2] += 1
            cnt[d1] += 1
        return ans
    unique3DigitEvenNumbers = totalNumbers