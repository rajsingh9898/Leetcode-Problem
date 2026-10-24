import sys
import os
import json
PREF_DAYS = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
def _solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        os._exit(0)
    it = iter(input_data)
    out = []
    append = out.append
    pref = PREF_DAYS
    for line in it:
        line = line.strip()
        if not line:
            continue
        arriveAlice = json.loads(line)
        leaveAlice = json.loads(next(it).strip())
        arriveBob = json.loads(next(it).strip())
        leaveBob = json.loads(next(it).strip())
        start = arriveAlice if arriveAlice > arriveBob else arriveBob
        end = leaveAlice if leaveAlice < leaveBob else leaveBob
        if start > end:
            append("0\n")
        else:
            d_start = pref[int(start[:2])] + int(start[3:])
            d_end = pref[int(end[:2])] + int(end[3:])
            append(f"{d_end - d_start + 1}\n")
    with open("user.out", "w") as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        return 0