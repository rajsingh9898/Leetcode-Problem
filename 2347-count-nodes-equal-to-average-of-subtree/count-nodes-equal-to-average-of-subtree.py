import gc
gc.disable()
class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            val = node.val
            s = val
            c = 1
            if node.left:
                ls, lc = dfs(node.left)
                s += ls
                c += lc
            if node.right:
                rs, rc = dfs(node.right)
                s += rs
                c += rc
            if s // c == val:
                ans += 1
            return s, c
        if root:
            dfs(root)
        return ans