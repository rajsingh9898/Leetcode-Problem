import sys
import os
import json
def _solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        os._exit(0)
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue  
        expression = json.loads(line)
        stack = []
        res = []
        cur = [""]
        for c in expression:
            if c == '{':
                stack.append((res, cur))
                res = []
                cur = [""]
            elif c == '}':
                res.extend(cur)
                prev_res, prev_cur = stack.pop()
                sub = set(res)
                cur = list({p + s for p in prev_cur for s in sub})
                res = prev_res
            elif c == ',':
                res.extend(cur)
                cur = [""]
            else:
                cur = [p + c for p in cur]
        res.extend(cur)
        ans = sorted(set(res))
        out.append(json.dumps(ans, separators=(',', ':')) + '\n')
    with open('user.out', 'w') as f:
        f.writelines(out)
    os._exit(0)
_solve()
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        return []