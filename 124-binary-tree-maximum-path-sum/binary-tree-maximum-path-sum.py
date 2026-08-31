from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def get_max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))
            current_path_sum = node.val + left_gain + right_gain
            if current_path_sum > max_sum:
                max_sum = current_path_sum
            return node.val + max(left_gain, right_gain)
        get_max_gain(root)
        return max_sum