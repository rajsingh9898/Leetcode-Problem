class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        intervals = []
        for c in first:
            l = first[c]
            r = last[c]
            valid = True
            i = l
            while i <= r:
                if first[s[i]] < l:
                    valid = False
                    break
                if last[s[i]] > r:
                    r = last[s[i]]
                i += 1
            if valid:
                intervals.append((r, l))
        intervals.sort()
        ans = []
        last_end = -1
        for r, l in intervals:
            if l > last_end:
                ans.append(s[l : r + 1])
                last_end = r
        return ans