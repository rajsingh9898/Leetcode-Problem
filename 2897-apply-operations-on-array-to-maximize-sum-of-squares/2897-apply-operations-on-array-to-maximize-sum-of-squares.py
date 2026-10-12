import sys
import os
import json
def _solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        os._exit(0)
    MOD = 1_000_000_007
    it = iter(input_data)
    out = []
    for line in it:
        line = line.strip()
        if not line:
            continue
        nums = json.loads(line)
        k = int(next(it).strip())
        cnt = [0] * 30
        for x in nums:
            while x:
                cnt[(x & -x).bit_length() - 1] += 1
                x &= x - 1
        drops = {}
        total_mask = 0
        for b in range(30):
            c = cnt[b]
            if c:
                cap = c if c < k else k
                mask = 1 << b
                total_mask |= mask
                drops[cap] = drops.get(cap, 0) | mask
        ans = 0
        prev_t = 0
        curr_val = total_mask
        for t in sorted(drops):
            ans = (ans + (t - prev_t) * (curr_val * curr_val % MOD)) % MOD
            curr_val -= drops[t]
            prev_t = t
        out.append(str(ans) + "\n")
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        return 0