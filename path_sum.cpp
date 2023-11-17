/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) {
            return false;
        } else {
            bool left = false, right = false;
            targetSum = targetSum - (*root).val;
            if (((*root).left == nullptr) && ((*root).right == nullptr)) {
                return targetSum == 0;
            }
            if ((*root).left != nullptr) {
                left = hasPathSum((*root).left, targetSum);
            }
            if ((*root).right != nullptr) {
                right = hasPathSum((*root).right, targetSum);
            }
            return left || right;
        }
    }
};
