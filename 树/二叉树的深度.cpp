/*
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
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
    int maxDepth(TreeNode* root) {
        //BFS
        if (root==NULL) return 0;
        queue<TreeNode*> q;
        int depth = 0;
        q.push(root);
        while (!q.empty()){
            int size = q.size();
            for (int i = 0; i<size; i++){
                TreeNode* node = q.front();
                q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right); 
            }
            depth++;
        }
        return depth;
    //DFS recursive
    //     if (root==nullptr){
    //         return 0;
    //     }
    //     int l = maxDepth(root->left);
    //     int r = maxDepth(root->right);
    //     return (l>r)?(l+1):(r+1);

    }

};