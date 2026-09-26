class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        parts = s.replace(')', '(').split('(')
        parts[1::2] = [d.get(k, '?') for k in parts[1::2]]
        return "".join(parts)