import functools

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    @functools.lru_cache(maxsize=None)
    def mis_without_root(self, root):
        # self.counter += 1
        # print(self.counter)
        if root.left == None and root.right == None:
            return 0
        else:
            x = y = 0
            if root.left != None:
                x = self.mis(root.left)
            if root.right != None:
                y = self.mis(root.right)
            return x + y

    @functools.lru_cache(maxsize=None)
    def mis(self, root):
        # self.counter += 1
        # print(self.counter)
        if root.left == None and root.right == None:
            return root.val
        else:
            x1 = y1 = x2 = y2 = 0
            if root.left != None:
                x1 = self.mis(root.left)
                x2 = self.mis_without_root(root.left)
            if root.right != None:
                y1 = self.mis(root.right)
                y2 = self.mis_without_root(root.right)
            return max(x1 + y1, x2 + y2 + root.val)

    def rob(self, root: Optional[TreeNode]) -> int:
        return self.mis(root)
        
