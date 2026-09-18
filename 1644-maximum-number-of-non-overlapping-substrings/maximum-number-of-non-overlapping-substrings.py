class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        chars = set(s)
        first = {c: s.find(c) for c in chars}
        last = {c: s.rfind(c) for c in chars}
        intervals = []
        for c in chars:
            l = first[c]
            r = last[c]
            valid = True
            changed = True
            while changed:
                changed = False
                for ch in chars:
                    f, e = first[ch], last[ch]
                    if l <= f <= r:
                        if e > r:
                            r = e
                            changed = True
                    elif f < l and e >= l:
                        if s.find(ch, l, r + 1) != -1:
                            valid = False
                            break
                if not valid:
                    break
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