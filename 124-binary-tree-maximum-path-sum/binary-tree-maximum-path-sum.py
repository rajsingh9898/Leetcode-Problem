class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            l = l if l > 0 else 0
            r = r if r > 0 else 0
            path = node.val + l + r
            if path > ans:
                ans = path
            return node.val + (l if l > r else r)
        dfs(root)
        return ans