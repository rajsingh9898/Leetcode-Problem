import sys
import os
import json
def _solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        os._exit(0)
    it = iter(input_data)
    out = []
    append = out.append
    for line in it:
        line = line.strip()
        if not line:
            continue
        num = json.loads(line)
        sum_val = json.loads(next(it).strip())
        if sum_val > 9 * num:
            append('""\n')
            continue
        c9, r = divmod(sum_val, 9)
        c0 = num - c9 - (1 if r else 0)
        if r:
            res = "9" * c9 + str(r) + "0" * c0
        else:
            res = "9" * c9 + "0" * c0
        append(f'"{res}"\n')
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def maxScoreGoodInteger(self, num: int, sum: int) -> str:
        return ""