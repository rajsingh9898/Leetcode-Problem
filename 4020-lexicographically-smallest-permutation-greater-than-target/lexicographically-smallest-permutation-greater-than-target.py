from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        for i in range(n - 1, -1, -1):
            prefix = target[:i]
            prefix_counts = Counter(prefix)
            if any(prefix_counts[ch] > total_counts[ch] for ch in prefix_counts):
                continue
            rem_counts = total_counts - prefix_counts
            target_char = target[i]
            valid_char = None
            for code in range(ord(target_char) + 1, ord('z') + 1):
                ch = chr(code)
                if rem_counts[ch] > 0:
                    valid_char = ch
                    break
            if valid_char is not None:
                rem_counts[valid_char] -= 1
                suffix = []
                for code in range(ord('a'), ord('z') + 1):
                    ch = chr(code)
                    if rem_counts[ch] > 0:
                        suffix.append(ch * rem_counts[ch])
                return prefix + valid_char + "".join(suffix)
        return ""