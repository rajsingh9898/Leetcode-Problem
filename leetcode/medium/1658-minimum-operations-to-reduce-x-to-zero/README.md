# Minimum Operations to Reduce X to Zero

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this  **modifies**  the array for future operations.

Return  *the  **minimum number**  of operations to reduce* `x`  *to  **exactly***  `0`  *if it is possible**, otherwise, return* `-1`.

 

 **Example 1:** 

```
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

```

 **Example 2:** 

```
Input: nums = [5,6,7,8,9], x = 4
Output: -1

```

 **Example 3:** 

```
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104
- 1 <= x <= 109

## Solution

**Language:** Python  
**Runtime:** 119 ms (beats 26.28%)  
**Memory:** 30.9 MB (beats 71.36%)  
**Submitted:** 2026-09-23T15:34:12.106Z  

```py
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        left = 0
        cur = 0
        while left < n and cur + nums[left] <= x:
            cur += nums[left]
            left += 1
        min_ops = left if cur == x else float('inf')
        left -= 1
        right = n - 1
        while right >= 0:
            cur += nums[right]
            while left >= 0 and (cur > x or left >= right):
                cur -= nums[left]
                left -= 1
            if cur == x:
                ops = (left + 1) + (n - right)
                if ops < min_ops:
                    min_ops = ops
            if left < 0 and cur >= x:
                break
            right -= 1
        return min_ops if min_ops != float('inf') else -1
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)