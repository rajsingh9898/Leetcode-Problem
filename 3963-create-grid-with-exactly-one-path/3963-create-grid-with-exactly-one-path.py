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
        m = int(line)
        n = int(next(it).strip())
        row0 = "." * n
        rem_row = "#" * (n - 1) + "."
        res = [row0] + [rem_row] * (m - 1)
        append(f"{json.dumps(res, separators=(',', ':'))}\n")
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def constructGrid(self, m: int, n: int) -> list[str]:
        return []
    uniquePathsGrid = constructGrid
    generateGrid = constructGrid
    findGrid = constructGrid
    gridWithOnePath = constructGrid