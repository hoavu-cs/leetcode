# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        longest_path = 0

        def longest_one_side_path(node):
            nonlocal longest_path 
            if node == None:
                return 0
            else:
                x = longest_one_side_path(node.left)
                y = longest_one_side_path(node.right)
                longest_path = max(longest_path, x + y + 1)
                return max(x, y) + 1
        
        longest_one_side_path(root)
        return longest_path - 1
