class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        stack = [root]
        order = []
        stack_pop = stack.pop
        stack_append = stack.append
        order_append = order.append
        while stack:
            curr = stack_pop()
            order_append(curr)
            if curr.left:
                stack_append(curr.left)
            if curr.right:
                stack_append(curr.right)
        ans = 0
        sums = []
        counts = []
        sums_pop = sums.pop
        counts_pop = counts.pop
        sums_append = sums.append
        counts_append = counts.append
        for node in reversed(order):
            left = node.left
            right = node.right
            val = node.val
            if not left and not right:
                ans += 1
                sums_append(val)
                counts_append(1)
            else:
                s = val
                c = 1
                if right:
                    s += sums_pop()
                    c += counts_pop()
                if left:
                    s += sums_pop()
                    c += counts_pop()
                if s // c == val:
                    ans += 1
                sums_append(s)
                counts_append(c)
        return ans