'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 
 

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 
 

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = None
        self.pre = None
        # def in_order(curr):
        #     if not curr: return
        #     in_order(curr.left)
        #     if not self.pre: 
        #         self.head = curr
        #     else:
        #         self.pre.right, curr.left = curr, self.pre
        #     self.pre = curr
        #     in_order(curr.right)
        # in_order(root)
        # if self.head and self.pre:
        #     self.head.left, self.pre.right = self.pre, self.head
        # return self.head

        #iterative in_order search
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                # res.append(root.val)
                if not self.pre: self.head = root
                else:
                    self.pre.right, root.left = root, self.pre
                self.pre = root
                root = root.right
        if self.head and self.pre:
            self.head.left, self.pre.right = self.pre, self.head
        return self.head