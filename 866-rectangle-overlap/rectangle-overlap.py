class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x1_p, y1_p, x2_p, y2_p = rec2
        return (
            min(x2, x2_p) > max(x1, x1_p) and
            min(y2, y2_p) > max(y1, y1_p)
        )