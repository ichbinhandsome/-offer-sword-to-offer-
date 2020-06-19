/*
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        //双端队列
        deque<TreeNode*> q;
        q.push_back(root);
        int count = 1;
        while (!q.empty()){
            int n = q.size();
            vector<int> temp;
            for (int i = 0; i<n;i++){   
                if (count % 2 == 0){
                    TreeNode* node = q.back();
                    temp.push_back(node->val);
                    q.pop_back();
                    if (node->right) q.push_front(node->right);
                    if (node->left) q.push_front(node->left);
                }else{
                    TreeNode* node = q.front();
                    q.pop_front();
                    temp.push_back(node->val);
                    if (node->left) q.push_back(node->left);
                    if (node->right) q.push_back(node->right);
                }
            }
            count ++;
            res.push_back(temp);
        }
        return res;
    }
};