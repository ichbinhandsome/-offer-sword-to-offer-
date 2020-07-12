/*
''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
*/

class Solution {
public:
    bool helper(int left, int right,vector<int>& postorder){
        if (left>=right) return true;
        int i = left;
        while (postorder[i] < postorder[right]) i++;
        int temp = i;
        while (postorder[i] > postorder[right]) i++;
        return i == right && helper(left, i-1, postorder) && helper(i,right-1,postorder);
    }
    bool verifyPostorder(vector<int>& postorder) {
        return helper(0,postorder.size()-1,postorder);
    }
};