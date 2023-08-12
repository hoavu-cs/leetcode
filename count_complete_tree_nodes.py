# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        res = 0
        left = root.left
        right = root.right

        left_right_most_depth = 0
        right_right_most_depth = 0

        while left:
            left_right_most_depth += 1
            left = left.right
        while right:
            right_right_most_depth += 1
            right = right.right

        if left_right_most_depth >  right_right_most_depth:
            res += 2**left_right_most_depth-1
            res += self.countNodes(root.right)
            return res + 1
        else:
            res += 2**right_right_most_depth - 1
            res += self.countNodes(root.left)
            return res + 1
