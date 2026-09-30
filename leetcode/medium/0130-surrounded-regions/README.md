# Surrounded Regions

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an `m x n` matrix `board` containing  **letters**  `'X'` and `'O'`,  **capture regions**  that are  **surrounded** :

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

To capture a  **surrounded region**, replace all `'O'`s with `'X'`s  **in-place**  within the original board. You do not need to return anything.

 

 **Example 1:** 

 **Input:**  board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

 **Output:**  [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

 **Explanation:** 

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

 **Example 2:** 

 **Input:**  board = [["X"]]

 **Output:**  [["X"]]

 

 **Constraints:** 

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 22.1 MB (beats 98.68%)  
**Submitted:** 2026-09-20T19:42:45.969Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/surrounded-regions/)