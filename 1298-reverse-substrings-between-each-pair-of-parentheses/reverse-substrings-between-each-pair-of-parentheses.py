class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        res = []
        i = 0
        step = 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i] 
                step = -step
            else:
                res.append(s[i])
            i += step
        return "".join(res)