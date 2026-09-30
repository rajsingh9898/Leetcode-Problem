# Find X Value of Array I

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array of  **positive**  integers `nums`, and a  **positive**  integer `k`.

You are allowed to perform an operation  **once**  on `nums`, where in each operation you can remove any  **non-overlapping**  prefix and suffix from `nums` such that `nums` remains  **non-empty**.

You need to find the  **x-value**  of `nums`, which is the number of ways to perform this operation so that the  **product**  of the remaining elements leaves a  *remainder*  of `x` when divided by `k`.

Return an array `result` of size `k` where `result[x]` is the  **x-value**  of `nums` for `0 <= x <= k - 1`.

A  **prefix**  of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A  **suffix**  of an array is a subarray that starts at any point within the array and extends to the end of the array.

 **Note**  that the prefix and suffix to be chosen for the operation can be  **empty**.

 

 **Example 1:** 

 **Input:**  nums = [1,2,3,4,5], k = 3

 **Output:**  [9,2,4]

 **Explanation:** 

- For x = 0, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove nums[2] == 3.
- For x = 1, the possible operations are: Remove the empty prefix and the suffix [2, 3, 4, 5]. nums becomes [1]. Remove the prefix [1, 2, 3] and the suffix [5]. nums becomes [4].
- For x = 2, the possible operations are: Remove the empty prefix and the suffix [3, 4, 5]. nums becomes [1, 2]. Remove the prefix [1] and the suffix [3, 4, 5]. nums becomes [2]. Remove the prefix [1, 2, 3] and the empty suffix. nums becomes [4, 5]. Remove the prefix [1, 2, 3, 4] and the empty suffix. nums becomes [5].

 **Example 2:** 

 **Input:**  nums = [1,2,4,8,16,32], k = 4

 **Output:**  [18,1,2,0]

 **Explanation:** 

- For x = 0, the only operations that do not result in x = 0 are: Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2]. Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1]. Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
- For x = 1, the only possible operation is: Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
- For x = 2, the possible operations are: Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2]. Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
- For x = 3, there is no possible way to perform the operation.

 **Example 3:** 

 **Input:**  nums = [1,1,2,1,1], k = 2

 **Output:**  [9,6]

 

 **Constraints:** 

- 1 <= nums[i] <= 109
- 1 <= nums.length <= 105
- 1 <= k <= 5

## Solution

**Language:** Python  
**Runtime:** 55 ms (beats 100.00%)  
**Memory:** 34.2 MB (beats 52.63%)  
**Submitted:** 2026-09-21T06:19:47.838Z  

```py
class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        total = n * (n + 1) // 2
        if k == 1:
            return [total]
        if k == 2:
            dp1 = ans1 = 0
            for x in nums:
                if x % 2:
                    dp1 += 1
                else:
                    dp1 = 0
                ans1 += dp1
            return [total - ans1, ans1]
        if k == 3:
            dp1 = dp2 = 0
            ans1 = ans2 = 0
            for x in nums:
                v = x % 3
                if v == 1:
                    dp1 += 1
                elif v == 2:
                    dp1, dp2 = dp2, dp1 + 1
                else:
                    dp1 = dp2 = 0
                ans1 += dp1
                ans2 += dp2
            return [total - ans1 - ans2, ans1, ans2]
        if k == 4:
            dp1 = dp2 = dp3 = 0
            ans1 = ans2 = ans3 = 0
            for x in nums:
                v = x % 4
                if v == 1:
                    dp1 += 1
                elif v == 3:
                    dp1, dp3 = dp3, dp1 + 1
                elif v == 2:
                    dp1, dp2, dp3 = 0, dp1 + dp3 + 1, 0
                else:
                    dp1 = dp2 = dp3 = 0
                ans1 += dp1
                ans2 += dp2
                ans3 += dp3
            return [total - ans1 - ans2 - ans3, ans1, ans2, ans3]
        dp1 = dp2 = dp3 = dp4 = 0
        ans1 = ans2 = ans3 = ans4 = 0
        for x in nums:
            v = x % 5
            if v == 1:
                dp1 += 1
            elif v == 2:
                dp1, dp2, dp3, dp4 = dp3, dp1 + 1, dp4, dp2
            elif v == 3:
                dp1, dp2, dp3, dp4 = dp2, dp4, dp1 + 1, dp3
            elif v == 4:
                dp1, dp2, dp3, dp4 = dp4, dp3, dp2, dp1 + 1
            else:
                dp1 = dp2 = dp3 = dp4 = 0
            ans1 += dp1
            ans2 += dp2
            ans3 += dp3
            ans4 += dp4
        return [total - ans1 - ans2 - ans3 - ans4, ans1, ans2, ans3, ans4]
```

---

[View on LeetCode](https://leetcode.com/problems/find-x-value-of-array-i/)