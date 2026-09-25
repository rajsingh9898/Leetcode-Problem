from itertools import product
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        if "{" not in expression:
            return sorted(set(expression.split(",")))
        groups = [[]]
        level = 0
        i = 0
        n = len(expression)
        while i < n:
            c = expression[i]
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1
                i += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
                i += 1
            elif c == ',' and level == 0:
                groups.append([])
                i += 1
            elif level == 0:
                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                groups[-1].append([expression[i:j]])
                i = j
            else:
                i += 1
        ans = set()
        for group in groups:
            if len(group) == 1:
                ans.update(group[0])
            elif group:
                for prod in product(*group):
                    ans.add("".join(prod))
        return sorted(ans)