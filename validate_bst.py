from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidWithMinMax(self, root):
        if root.left == None and root.right == None:
            return True, root.val, root.val
        else:
            is_valid_left, is_valid_right = True, True
            left_min, left_max, right_min, right_max = None, None, None, None
            is_valid = True

            if root.left != None:
                is_valid_left, left_min, left_max = self.isValidWithMinMax(root.left)
            if root.right != None:
                is_valid_right, right_min, right_max = self.isValidWithMinMax(root.right)
            
            if left_max != None:
                is_valid = root.val > left_max
            if right_min != None:
                is_valid = is_valid and root.val < right_min

            is_valid = is_valid_left and is_valid_right and is_valid

            if not left_min:
                left_min = root.val
            if not right_max:
                right_max = root.val

            return is_valid, left_min, right_max

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidWithMinMax(root)[0]
        
