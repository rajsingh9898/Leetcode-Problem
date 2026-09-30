class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        safe_stack = []
        for r in range(m):
            if board[r][0] == 'O':
                board[r][0] = '#'
                safe_stack.append((r, 0))
            if board[r][n - 1] == 'O':
                board[r][n - 1] = '#'
                safe_stack.append((r, n - 1))
        for c in range(1, n - 1):
            if board[0][c] == 'O':
                board[0][c] = '#'
                safe_stack.append((0, c))
            if board[m - 1][c] == 'O':
                board[m - 1][c] = '#'
                safe_stack.append((m - 1, c))
        while safe_stack:
            r, c = safe_stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    safe_stack.append((nr, nc))
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'