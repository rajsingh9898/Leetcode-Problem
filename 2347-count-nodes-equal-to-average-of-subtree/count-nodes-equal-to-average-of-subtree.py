class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ans = 0
        for node in reversed(order):
            s = node.val
            c = 1
            left = node.left
            if left:
                s += left.s
                c += left.c
            right = node.right
            if right:
                s += right.s
                c += right.c
            if node.val == s // c:
                ans += 1
            node.s = s
            node.c = c
        return ans