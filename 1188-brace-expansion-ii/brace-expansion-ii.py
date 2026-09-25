class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        if "{" not in expression:
            return [expression]
        stack = [expression]
        seen = {expression}
        res = set()
        while stack:
            s = stack.pop()
            if "{" not in s:
                res.add(s)
                continue
            j = s.find("}")
            i = s.rfind("{", 0, j)
            head = s[:i]
            tail = s[j + 1:]
            for sub in s[i + 1:j].split(","):
                nxt = head + sub + tail
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return sorted(res)