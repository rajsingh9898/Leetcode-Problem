_NON_ALNUM = "".join(chr(i) for i in range(128) if not chr(i).isalnum())
_TABLE = str.maketrans("", "", _NON_ALNUM)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # C-level bulk deletion, lowercase, and slicing
        cleaned = s.translate(_TABLE).lower()
        return cleaned == cleaned[::-1]