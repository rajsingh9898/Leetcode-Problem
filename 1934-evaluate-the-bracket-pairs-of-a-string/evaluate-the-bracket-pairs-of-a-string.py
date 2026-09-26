class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = dict(knowledge)
        parts = s.split('(')
        res = [parts[0]]
        for part in parts[1:]:
            key, rest = part.split(')', 1)
            res.append(mapping.get(key, '?'))
            res.append(rest)
        return "".join(res)