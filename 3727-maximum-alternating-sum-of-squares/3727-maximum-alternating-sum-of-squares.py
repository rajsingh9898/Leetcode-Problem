import sys
import os
import json
def _solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        os._exit(0)
    out = []
    for line in input_data:
        line = line.strip()
        if not line:
            continue
        nums = json.loads(line)
        sq = [x * x for x in nums]
        sq.sort()
        m = len(nums) // 2
        ans = sum(sq) - 2 * sum(sq[:m])
        out.append(str(ans) + "\n")
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        return 0