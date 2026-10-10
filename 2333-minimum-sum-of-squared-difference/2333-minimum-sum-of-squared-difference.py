class Solution:
    __slots__ = ()
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)] 
        if sum(diff) <= k:
            return 0
        diff.sort(reverse=True)
        n = len(diff)
        diff.append(0) 
        for i in range(n):
            gap = diff[i] - diff[i + 1]
            if not gap:
                continue
            needed = (i + 1) * gap
            if k >= needed:
                k -= needed
            else:
                q, r = divmod(k, i + 1)
                target = diff[i] - q 
                ans = (i + 1 - r) * target * target + r * (target - 1) * (target - 1) 
                if i + 1 < n:
                    ans += sum([x * x for x in diff[i + 1 : n]])
                return ans
        return 0