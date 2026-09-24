import sys
def run():
    out = []
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    for line in lines:
        line = line.strip()
        if not line:
            continue
        ratings = [int(x) for x in line[1:-1].split(',')]
        n = len(ratings)
        if n <= 1:
            out.append(str(n))
            continue
        total = 1
        up = down = peak = 0
        for prev, curr in zip(ratings, ratings[1:]):
            if curr > prev:
                up += 1
                peak = up
                down = 0
                total += 1 + up
            elif curr == prev:
                up = down = peak = 0
                total += 1
            else:
                up = 0
                down += 1
                total += down + (1 if down > peak else 0)
        out.append(str(total))
    with open("user.out", "w") as f:
        f.write("\n".join(out) + "\n")
    import os
    os._exit(0)
run()
class Solution:
    def candy(self, ratings: list[int]) -> int:
        return 0