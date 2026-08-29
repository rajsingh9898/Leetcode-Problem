class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        order = sorted(range(n), key=nums.__getitem__)
        sorted_vals = [nums[i] for i in order]
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_vals[j] - sorted_vals[j - 1] <= limit:
                j += 1
            indices = sorted(order[i:j])
            for k in range(j - i):
                ans[indices[k]] = sorted_vals[i + k]
            i = j
        return ans