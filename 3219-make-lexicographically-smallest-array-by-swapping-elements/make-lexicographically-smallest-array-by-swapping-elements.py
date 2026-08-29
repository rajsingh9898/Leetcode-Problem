class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        ans = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and sorted_pairs[j + 1][0] - sorted_pairs[j][0] <= limit:
                j += 1
            indices = sorted(sorted_pairs[k][1] for k in range(i, j + 1))
            for k in range(len(indices)):
                ans[indices[k]] = sorted_pairs[i + k][0]
            i = j + 1
        return ans