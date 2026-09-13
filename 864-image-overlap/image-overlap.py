class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        A = B = 0
        countA = countB = 0
        for r in range(n):
            row1, row2 = img1[r], img2[r]
            offset = r * 64
            for c in range(n):
                if row1[c]:
                    A |= 1 << (offset + c)
                    countA += 1
                if row2[c]:
                    B |= 1 << (offset + c)
                    countB += 1
        upper_bound = min(countA, countB)
        if upper_bound == 0:
            return 0
        ans = 0
        dy_order = [0]
        for d in range(1, n):
            dy_order.extend((d, -d))
        dx_order = [0]
        for d in range(1, n):
            dx_order.extend((d, -d))
        for dy in dy_order:
            if (n - abs(dy)) * n <= ans:
                continue
            base = dy * 64
            for dx in dx_order:
                if (n - abs(dy)) * (n - abs(dx)) <= ans:
                    continue
                s = base + dx
                if s >= 0:
                    val = (A & (B >> s)).bit_count()
                else:
                    val = ((A >> -s) & B).bit_count()
                if val > ans:
                    ans = val
                    if ans == upper_bound:
                        return ans
        return ans