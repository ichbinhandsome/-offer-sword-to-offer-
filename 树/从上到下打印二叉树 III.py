'''
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
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        count = 1
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue)):
                if count % 2 == 0:
                    node = queue.pop()
                    temp.append(node.val)
                    # if node.right: queue.insert(0,node.right)
                    # if node.left: queue.insert(0,node.left)
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                else: 
                    node = queue.popleft()
                    temp.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            # if count % 2 == 0: temp[:] = temp[::-1]
            count += 1
            res.append(temp)
        return res