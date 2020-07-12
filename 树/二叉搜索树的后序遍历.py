'''
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
'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        #递归判断
        #思路：列表最后一个为根节点的值，然后划分左右子树，比根节点小的值是左子树的后序遍历
        #比根节点大的值是右子树的后序遍历。然后递归判断左右子树（看最后一个节点的索引是否为之前root的
        #索引）。
        # def helper(left, right):
        #     #递归终止条件（节点数<=1）
        #     if left >= right: return True
        #     index = left
        #     while postorder[index] < postorder[right]: index+=1
        #     m = index
        #     l = helper(left,index-1)
        #     while postorder[index] > postorder[right]: index+=1
        #     r = helper(m,right-1)
        #     #判断是否为root索引
        #     if index == right: return l and r #每一次层的返回值
        #     return False #层返回值
        # return helper(0,len(postorder)-1)

        #单调栈
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True
