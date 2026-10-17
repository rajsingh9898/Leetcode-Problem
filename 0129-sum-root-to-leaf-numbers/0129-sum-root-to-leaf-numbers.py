class Solution:
    __slots__ = ()
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node: TreeNode, acc: int) -> int:
            acc = acc * 10 + node.val
            left, right = node.left, node.right
            if not left and not right:
                return acc
            total = 0
            if left:
                total += dfs(left, acc)
            if right:
                total += dfs(right, acc)
            return total
        return dfs(root, 0)