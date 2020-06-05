/*
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        bool res = true;
        if (root != NULL){
            res = helepr(root->left, root->right);
        }
        return res;
    }
    bool helepr(TreeNode* node1, TreeNode* node2){
        if (node1 == NULL && node2 == NULL){
            return true;
        }
        if (node1 == NULL || node2 == NULL || node1->val != node2->val){
            return false;
        }
        return helepr(node1->left, node2->right) && helepr(node1->right, node2->left);
    }
};