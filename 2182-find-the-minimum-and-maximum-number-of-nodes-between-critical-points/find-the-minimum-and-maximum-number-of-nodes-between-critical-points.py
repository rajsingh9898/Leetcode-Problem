from typing import Optional
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev = head
        curr = head.next
        idx = 1
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_cp == -1:
                    first_cp = idx
                else:
                    dist = idx - last_cp
                    if dist < min_dist:
                        min_dist = dist
                last_cp = idx
            prev = curr
            curr = curr.next
            idx += 1
        if first_cp == -1 or first_cp == last_cp:
            return [-1, -1]
        return [min_dist, last_cp - first_cp]