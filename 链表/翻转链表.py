'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        # curr = head
        # second = head.next
        # head.next = None
        # while second:
        #     temp = second.next
        #     second.next = curr
        #     curr = second
        #     second = temp
        # return curr
        #         result = None

#链表翻转，每次翻转一个指针， 使用pre和curr, pre->curr， curr->pre
        pre = None
        curr = head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = pre
            pre = temp
        return pre
