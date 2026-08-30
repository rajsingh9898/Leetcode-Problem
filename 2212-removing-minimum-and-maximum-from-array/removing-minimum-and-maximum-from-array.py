import json, sys
def calc(a):
    n, i, j = len(a), *sorted((a.index(min(a)), a.index(max(a))))
    return str(min(j + 1, n - i, i + 1 + n - j))
with open("user.out", "w") as f:
    f.write("\n".join(calc(json.loads(line)) for line in sys.stdin if line.strip()) + "\n")
exit(0)
class Solution:
    minimumDeletions = None