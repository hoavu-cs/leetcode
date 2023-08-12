from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf

        def max_path_sum_end(root):
            # find the maximum path sum in which root is an end point
            nonlocal res
            max_left = max_right = 0
            if root.left == None and root.right == None:
                root.val
            if root.left:
                max_left = max(0, max_path_sum_end(root.left))
            if root.right:
                max_right = max(0, max_path_sum_end(root.right))
            res = max(res, max_left + max_right + root.val)
            return max(root.val, max_left + root.val, max_right + root.val)
        
        max_path_sum_end(root)

        return res
