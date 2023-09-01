# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif (not root1 and root2) or (root1 and not root2):
            return False
        else:
            if root1.val != root2.val:
                return False
            if (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
            (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)):
                return True
            else:
                return False

