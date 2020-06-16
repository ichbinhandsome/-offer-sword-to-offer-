'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]


示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return
        #后序遍历 递归
        def helper(node,p,q):
            if not node or node == p or node == q: return node
            l = helper(node.left,p,q)
            r = helper(node.right,p,q)
            if not l: return r
            if not r: return l
            return node
        return helper(root,p,q)
        #搜寻路径
        # s1, s2 = [], []
        # def route(root,node,stack):
        #     if not root: return False
        #     stack.append(root)
        #     if root == node: 
        #         return True
        #     l = route(root.left,node,stack)
        #     r = route(root.right,node,stack)
        #     if l or r: return True
        #     stack.pop()
        # route(root,p,s1)
        # route(root,q,s2)
        # for i in s1[::-1]:
        #     if i in s2: return i
        # return