'''
给定一棵二叉搜索树，请找出其中第k大的节点。


示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return

        # three methods:
    
        # stack = []
        # seq = []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     seq.append(root.val)
        #     root = root.right
        # # print(seq)            
        # return seq[-k]

        self.k = k
        def inverse_in_oder(node):
            if not node: return
            l = inverse_in_oder(node.right)
            self.k -= 1
            if self.k == 0: 
                return node.val
            r = inverse_in_oder(node.left)
            return l or r
        return inverse_in_oder(root)

        # self.seq = []
        # def in_order(node):
        #     if not node: return
        #     in_order(node.left)
        #     self.seq.append(node.val)
        #     in_order(node.right)
        # in_order(root)
        # return self.seq[-k]

