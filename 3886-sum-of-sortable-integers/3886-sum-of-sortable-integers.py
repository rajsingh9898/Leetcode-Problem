class Solution:
    __slots__ = ()
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        pref = [0] * n
        for i in range(n - 1):
            pref[i + 1] = pref[i] + (1 if nums[i] > nums[i + 1] else 0)
        total_drops = pref[n - 1]
        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1
        if total_drops == 0:
            return sum(divisors)
        next_drop = [n] * n
        nxt = n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nxt = i
            next_drop[i] = nxt
        def is_sortable(k: int) -> bool:
            m = n // k
            prev_max = -1
            for i in range(m):
                L = i * k
                R = L + k - 1
                cnt = pref[R] - pref[L]
                if cnt > 1:
                    return False
                if cnt == 0:
                    cur_min = nums[L]
                    cur_max = nums[R]
                else:
                    if nums[R] > nums[L]:
                        return False
                    j = next_drop[L]
                    cur_min = nums[j + 1]
                    cur_max = nums[j]
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
            return True
        ans = 0
        for k in divisors:
            if k == 1 or total_drops > n // k:
                continue
            if is_sortable(k):
                ans += k

        return ans