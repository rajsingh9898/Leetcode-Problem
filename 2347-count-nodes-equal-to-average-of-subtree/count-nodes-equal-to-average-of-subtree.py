class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = (left >> 12) + (right >> 12) + node.val
            c = (left & 4095) + (right & 4095) + 1
            if node.val == s // c:
                ans += 1
            return (s << 12) | c
        dfs(root)
        return ans