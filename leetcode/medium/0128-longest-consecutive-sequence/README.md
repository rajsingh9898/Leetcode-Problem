# Longest Consecutive Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an unsorted array of integers `nums`, return  *the length of the longest consecutive elements sequence.* 

You must write an algorithm that runs in `O(n)` time.

 

 **Example 1:** 

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

 **Example 2:** 

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

 **Example 3:** 

```
Input: nums = [1,0,1,2]
Output: 3

```

 

 **Constraints:** 

- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 98.65%)  
**Memory:** 36.6 MB (beats 67.37%)  
**Submitted:** 2026-09-20T16:10:41.590Z  

```py
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        ans = 0
        while s:
            if len(s) <= ans:
                break
            x = s.pop()
            l = x - 1
            while l in s:
                s.remove(l)
                l -= 1
            r = x + 1
            while r in s:
                s.remove(r)
                r += 1
            ans = max(ans, r - l - 1)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)