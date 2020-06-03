'''
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        # root.left, root.right = root.right, root.left
        # self.mirrorTree(root.left)
        # self.mirrorTree(root.right)
        # return root

        #dfs
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root

        #BFS 
        queue= [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    node.left, node.right = node.right, node.left
                    queue.append(node.left)
                    queue.append(node.right)
        return root