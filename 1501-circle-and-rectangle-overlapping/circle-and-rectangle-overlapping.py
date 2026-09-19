class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        near_x = x1 if xCenter < x1 else (x2 if xCenter > x2 else xCenter)
        near_y = y1 if yCenter < y1 else (y2 if yCenter > y2 else yCenter)
        dx = xCenter - near_x
        dy = yCenter - near_y
        return dx * dx + dy * dy <= radius * radius