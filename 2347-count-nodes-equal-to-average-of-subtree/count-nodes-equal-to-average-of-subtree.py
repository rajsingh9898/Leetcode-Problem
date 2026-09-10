class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        matching_nodes = 0
        def dfs(node):
            nonlocal matching_nodes
            if not node:
                return 0, 0
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)
            t_sum = l_sum + r_sum + node.val
            t_cnt = l_cnt + r_cnt + 1
            if node.val == t_sum // t_cnt:
                matching_nodes += 1
            return t_sum, t_cnt
        dfs(root)
        return matching_nodes