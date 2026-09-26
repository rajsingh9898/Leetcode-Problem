class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        if '(' not in s:
            return s
        d = dict(knowledge)
        get = d.get 
        parts = s.replace(')', '(').split('(')
        parts[1::2] = [get(k, '?') for k in parts[1::2]]
        return "".join(parts)