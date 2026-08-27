class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        rem = [0] * 26
        for ch in s:
            rem[ord(ch) - 97] += 1
        matched = 0
        while matched < n:
            c = ord(target[matched]) - 97
            if rem[c] > 0:
                rem[c] -= 1
                matched += 1
            else:
                break
        if matched == n:
            matched = n - 1
            rem[ord(target[n - 1]) - 97] += 1
        for i in range(matched, -1, -1):
            target_code = ord(target[i]) - 97
            chosen = -1
            for c in range(target_code + 1, 26):
                if rem[c] > 0:
                    chosen = c
                    break
            if chosen != -1:
                rem[chosen] -= 1
                suffix = []
                for c in range(26):
                    if rem[c] > 0:
                        suffix.append(chr(c + 97) * rem[c])
                return target[:i] + chr(chosen + 97) + "".join(suffix)
            if i > 0:
                rem[ord(target[i - 1]) - 97] += 1
        return ""