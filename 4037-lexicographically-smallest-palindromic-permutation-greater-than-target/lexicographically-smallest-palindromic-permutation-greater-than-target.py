from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [ch for ch, freq in cnt.items() if freq % 2 == 1]
        if (n % 2 == 0 and len(odd_chars) != 0) or (n % 2 == 1 and len(odd_chars) != 1):
            return ""
        mid_char = odd_chars[0] if odd_chars else ""
        m = n // 2
        half_cnt = [0] * 26
        for ch, freq in cnt.items():
            half_cnt[ord(ch) - 97] = freq // 2
        target_half_cnt = [0] * 26
        for i in range(m):
            target_half_cnt[ord(target[i]) - 97] += 1
        if target_half_cnt == half_cnt:
            candidate = target[:m] + mid_char + target[:m][::-1]
            if candidate > target:
                return candidate
        rem = list(half_cnt)
        matched = 0
        while matched < m:
            c = ord(target[matched]) - 97
            if rem[c] > 0:
                rem[c] -= 1
                matched += 1
            else:
                break
        if matched == m:
            matched = m - 1
            rem[ord(target[m - 1]) - 97] += 1
        for i in range(matched, -1, -1):
            target_c = ord(target[i]) - 97
            chosen = -1
            for c in range(target_c + 1, 26):
                if rem[c] > 0:
                    chosen = c
                    break
            if chosen != -1:
                rem[chosen] -= 1
                suffix = []
                for c in range(26):
                    if rem[c] > 0:
                        suffix.append(chr(c + 97) * rem[c])
                first_half = target[:i] + chr(chosen + 97) + "".join(suffix)
                return first_half + mid_char + first_half[::-1]
            if i > 0:
                rem[ord(target[i - 1]) - 97] += 1
        return ""