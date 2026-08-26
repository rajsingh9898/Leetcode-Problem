class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        left, right = 0, m
        while True:
            i = (left + right) // 2
            j = half - i
            nums1Left = nums1[i - 1] if i > 0 else float('-inf')
            nums1Right = nums1[i] if i < m else float('inf')
            nums2Left = nums2[j - 1] if j > 0 else float('-inf')
            nums2Right = nums2[j] if j < n else float('inf')
            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total % 2:
                    return min(nums1Right, nums2Right)
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            elif nums1Left > nums2Right:
                right = i - 1
            else:
                left = i + 1