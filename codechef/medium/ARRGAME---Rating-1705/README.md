# ARRGAME - Rating 1705

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Game on a Strip

Tzuyu gave Nayeon a strip of $N$ cells (numbered $1$ through $N$) for her birthday. This strip is described by a sequence $A_1, A_2, \ldots, A_N$, where for each valid $i$, the $i$-th cell is blocked if $A_i = 1$ or free if $A_i = 0$. Tzuyu and Nayeon are going to use it to play a game with the following rules:

- The players alternate turns; Nayeon plays first.
- Initially, both players are outside of the strip. However, note that afterwards during the game, their positions are always different.
- In each turn, the current player should choose a free cell and move there. Afterwards, this cell becomes blocked and the players cannot move to it again.
- If it is the current player's first turn, she may move to any free cell.
- Otherwise, she may only move to one of the left and right adjacent cells, i.e. from a cell $c$, the current player may only move to the cell $c-1$ or $c+1$ (if it is free).
- If a player is unable to move to a free cell during her turn, this player loses the game.

Nayeon and Tzuyu are very smart, so they both play optimally. Since it is Nayeon's birthday, she wants to know if she can beat Tzuyu. Find out who wins.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
### Output

For each test case, print a single line containing the string `"Yes"` if Nayeon wins the game or `"No"` if Tzuyu wins (without quotes).

### Constraints
- $1 \le T \le 40,000$
- $2 \le N \le 3\cdot 10^5$
- $0 \le A_i \le 1$ for each valid $i$
- $A_1 = A_N = 1$
- the sum of $N$ over all test cases does not exceed $10^6$
### Subtasks

 **Subtask #1 (50 points):**  $A_i = 0$ for each $i$ ($2 \le i \le N-1$)

 **Subtask #2 (50 points):**  original constraints

### Sample 1:
Input
Output

```
4
7
1 1 0 0 0 1 1
8
1 0 1 1 1 0 0 1
4
1 1 0 1
4
1 1 1 1
```

```
Yes
No
Yes
No
```

### Explanation:

 **Example case 1:**  Since both Nayeon and Tzuyu play optimally, Nayeon can start e.g. by moving to cell $4$, which then becomes blocked. Tzuyu has to pick either the cell $3$ or the cell $5$, which also becomes blocked. Nayeon is then left with only one empty cell next to cell $4$ (the one Tzuyu did not pick); after she moves there, Tzuyu is unable to move, so she loses the game.

 **Example case 2:**  Regardless of what cell Nayeon moves to at the start, Tzuyu will always be able to beat her.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T16:28:29.553Z  

```cpp
import sys
def solve():
    # Read all tokens using fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    num_test_cases = int(next(it))
    out = []
    for _ in range(num_test_cases):
        n = int(next(it))
        m1 = 0 
        m2 = 0 
        cur = 0
        for _ in range(n):
            val = next(it)
            if val == '0':
                cur += 1
            else:
                if cur > 0:
                    if cur > m1:
                        m2 = m1
                        m1 = cur
                    elif cur > m2:
                        m2 = cur
                    cur = 0
        if cur > 0:
            if cur > m1:
                m2 = m1
                m1 = cur
            elif cur > m2:
                m2 = cur
        if m1 > 0 and m1 % 2 == 1 and m2 <= (m1 - 1) // 2:
            out.append("Yes")
        else:
            out.append("No")
    sys.stdout.write("\n".join(out) + "\n")
if __name__ == '__main__':
    solve()
```

---

[View on CodeChef](https://www.codechef.com/problems/ARRGAME)