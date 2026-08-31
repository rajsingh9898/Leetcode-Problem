# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        a = head.val
        curr = head.next
        b = curr.val
        curr = curr.next
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        idx = 1
        while curr:
            c = curr.val
            if (b > a and b > c) or (b < a and b < c):
                if first_cp == -1:
                    first_cp = idx
                else:
                    dist = idx - last_cp
                    if dist < min_dist:
                        min_dist = dist
                last_cp = idx
            a = b
            b = c
            curr = curr.next
            idx += 1
        if first_cp == last_cp:
            return [-1, -1]
        return [min_dist, last_cp - first_cp]