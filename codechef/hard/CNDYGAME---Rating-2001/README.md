# CNDYGAME - Rating 2001

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

### Magical Candy Store

Chef and Chefu are at a magical candy store playing a game with the following rules:

- There are two candy counters; each of them stores an infinite number of candies. At any time, only one of the counters is open and the other is closed.
- Exactly one player is present at each of the counters. Initially, Chef is at the open counter and Chefu is at the closed counter.
- There is a sequence of $N$ distinct integers $A_1, A_2, \ldots, A_N$. The game consists of $R$ turns; in the $i$-th turn, the open counter offers only $C = A_{ (i-1) \% N + 1}$ candies to the player present at this counter. This player should choose a positive number of candies $M$ to accept, where $1 \le M \le C$.
- If this player accepts an odd number of candies, the players have to swap their positions (each player goes to the other counter).
- After each $N$ turns, the counter which was currently open is closed and the counter which was currently closed is opened.
- The primary goal of each player is to maximise his own number of candies after $R$ turns. As a second priority, each player wants to minimise the number of candies his opponent has after $R$ turns.

You should process $Q$ queries. In each query, you are given $R$ and you should find the number of candies Chef has after $R$ turns, assuming that both players play the game optimally. Since this number could be very large, compute it modulo $10^9 + 7$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains a single integer $Q$.
- Each of the next $Q$ lines contains a single integer $R$ describing a query.
### Output

For each query, print a single line containing one integer ― the maximum number of candies Chef can get, modulo $10^9+7$.

### Constraints
- $1 \le T \le 25$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- $A_1, A_2, \ldots, A_N$ are pairwise distinct
- $1 \le Q \le 10^5$
- $1 \le R \le 10^{12}$
- the sum of $N + Q$ over all test cases does not exceed $10^6$
### Subtasks

 **Subtask #1 (15 points):** 

- $N \le 10$
- $Q \le 35$
- $R \le 35$

 **Subtask #2 (85 points):**  original constraints

### Sample 1:
Input
Output

```
1
4
4 10 2 1
2
4
5
```

```
17
21
```

### Explanation:

 **Example case 1:**  In the $1$-st, $2$-nd and $3$-rd turn, Chef takes $4$, $10$ and $2$ candies ($16$ in total) respectively. In the $4$-th turn, Chef takes $1$ candy ($17$ in total; this is the answer to the first query), which is odd and hence he has to go to the counter which is closed. However, since $N = 4$ turns are just completed, the counter which was currently open closes and the other one (where Chef went) opens. In the $5$-th round, Chef can take $4$ candies, so he has $21$ candies.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T18:25:32.653Z  

```cpp
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/CNDYGAME)