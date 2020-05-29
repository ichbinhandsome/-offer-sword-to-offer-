/*
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0 || inorder.size() == 0) {
            return NULL;
        }
        TreeNode* treeNode = new TreeNode(preorder[0]);
        int mid = distance(begin(inorder), find(inorder.begin(), inorder.end(), preorder[0]));
        vector<int> left_pre(preorder.begin() + 1, preorder.begin() + mid + 1);
        vector<int> right_pre(preorder.begin() + mid + 1, preorder.end());
        vector<int> left_in(inorder.begin(), inorder.begin() + mid);
        vector<int> right_in(inorder.begin() + mid + 1, inorder.end());

        treeNode->left = buildTree(left_pre, left_in);
        treeNode->right = buildTree(right_pre, right_in);
        return treeNode;
    }
};