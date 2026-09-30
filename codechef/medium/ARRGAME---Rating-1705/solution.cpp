import sys
def solve():
    # Read all tokens using fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    num_test_cases = int(next(it))
    out = []
    for _ in range(num_test_cases):
        n = int(next(it))
        m1 = 0 
        m2 = 0 
        cur = 0
        for _ in range(n):
            val = next(it)
            if val == '0':
                cur += 1
            else:
                if cur > 0:
                    if cur > m1:
                        m2 = m1
                        m1 = cur
                    elif cur > m2:
                        m2 = cur
                    cur = 0
        if cur > 0:
            if cur > m1:
                m2 = m1
                m1 = cur
            elif cur > m2:
                m2 = cur
        if m1 > 0 and m1 % 2 == 1 and m2 <= (m1 - 1) // 2:
            out.append("Yes")
        else:
            out.append("No")
    sys.stdout.write("\n".join(out) + "\n")
if __name__ == '__main__':
    solve()