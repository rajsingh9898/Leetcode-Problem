class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
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
        return sorted(set(res))