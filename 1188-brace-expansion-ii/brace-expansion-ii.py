class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        n = len(expression)
        def parse_factor() -> set[str]:
            if expression[self.i] == '{':
                self.i += 1  
                res = parse_expr()
                self.i += 1 
                return res
            else:
                ch = expression[self.i]
                self.i += 1
                return {ch}
        def parse_term() -> set[str]:
            cur = {""}
            while self.i < n and expression[self.i] not in ',}':
                nxt = parse_factor()
                cur = {a + b for a in cur for b in nxt}
            return cur
        def parse_expr() -> set[str]:
            res = parse_term()
            while self.i < n and expression[self.i] == ',':
                self.i += 1  
                res |= parse_term()
            return res
        return sorted(parse_expr())