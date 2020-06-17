/*
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
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
    vector<vector<int>> res;
    vector<int>  path;
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        dfs(root,sum,path);
        return res;
    }
    void dfs(TreeNode* root, int sum, vector<int> path){
        if (root == NULL) return;
        path.push_back(root->val);
        if (root->val == sum && !root->left && !root->right){
            res.push_back(path);
        }
        dfs(root->left, sum-root->val,path);
        dfs(root->right,sum-root->val,path);
        path.pop_back();
    }
};