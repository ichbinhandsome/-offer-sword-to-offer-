'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。


示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        #先序遍历 二叉树最大深度
        def max_depth(node):
            if not node:
                return 0;
            return max(max_depth(node.left), max_depth(node.right))+1
        self.res = True
        def pre_order(node):
            if not node:
                return
            l = max_depth(node.left)
            r = max_depth(node.right)
            if abs(l - r) <= 1:
                pre_order(node.left)
                pre_order(node.right)
            else:
                self.res = False
                return
        pre_order(root)
        return self.res
