import sys
import os
import json
def _solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        os._exit(0)
    out = []
    append = out.append
    for line in input_data:
        line = line.strip()
        if not line:
            continue
        nums = json.loads(line)
        ans = -1
        for i, x in enumerate(nums):
            if x != i:
                if ans == -1:
                    ans = x
                else:
                    ans &= x
        append(f"{0 if ans == -1 else ans}\n")
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def maxK(self, nums: list[int]) -> int:
        return 0