class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        sb = s.encode('ascii')
        tb = target.encode('ascii')
        cnt = [0] * 26
        for b in sb:
            cnt[b - 97] += 1
        matched = 0
        while matched < n:
            c = tb[matched] - 97
            if cnt[c] > 0:
                cnt[c] -= 1
                matched += 1
            else:
                break
        if matched == n:
            matched = n - 1
            cnt[tb[n - 1] - 97] += 1
        for i in range(matched, -1, -1):
            target_c = tb[i] - 97
            for c in range(target_c + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    suffix = "".join(chr(k + 97) * cnt[k] for k in range(26) if cnt[k])
                    return target[:i] + chr(c + 97) + suffix
            if i > 0:
                cnt[tb[i - 1] - 97] += 1
        return ""