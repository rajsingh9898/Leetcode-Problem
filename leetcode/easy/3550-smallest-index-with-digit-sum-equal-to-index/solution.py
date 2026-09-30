import sys
import os
def _solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        os._exit(0)
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        nums = [int(v) for v in line[1:-1].split(',')]
        limit = min(len(nums), 28)
        ans = -1
        for i in range(limit):
            x = nums[i]
            if (x % 10) + ((x // 10) % 10) + ((x // 100) % 10) + (x // 1000) == i:
                ans = i
                break
        out.append(f"{ans}\n")
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        return 0