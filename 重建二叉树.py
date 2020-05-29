'''
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
'''
#思路： 根据前序遍历list第一个元素即为root.val，再在中序遍历中找到root.val的索引i，中序遍历[:i]中为所有左子树的元素,
#       中序遍历[i+1:]中为所有右子树的元素。 接下来为了递归构建树，我们需要在前序遍历list中分别找到左子树的root和右子树的root,
#       由前序遍历的性质可知，右子树所有的元素是一个连续的子序列，同理左子树也是，而这个连续的子序列中的第一个元素即为它对应的root。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #递归终止条件
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])

        i = inorder.index(root.val)
        #在中序遍历中找到左右子树对应的序列
        inorder_left = inorder[:i]
        inorder_right = inorder[i+1:]
        
        j = len(inorder_left)
        #在前序遍历中找到左右子树对应的序列
        preorder_left = preorder[1:j+1]
        preorder_right = preorder[j+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right,inorder_right)
        return root

