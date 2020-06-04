'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        #递归
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        #迭代
        # first, second = l1, l2
        # dummy = ListNode(0)
        # flag = dummy
        # while first and second:
        #     if first.val < second.val:
        #         flag.next = first
        #         flag = flag.next
        #         first = first.next
        #     else:
        #         flag.next = second
        #         flag = flag.next
        #         second = second.next
        # if not first and not second:
        #     return dummy.next
        # elif not first:
        #     flag.next = second
        #     return dummy.next
        # else:
        #     flag.next = first
        #     return dummy.next