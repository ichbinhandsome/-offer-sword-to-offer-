/*
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //双指针
        if (head == NULL){
            return head;
        }
        ListNode * cur = NULL, *pre = head;
        while ( pre!= NULL){
            ListNode* t = pre->next;
            pre->next  = cur;
            cur = pre;
            pre = t;
        }
        return cur;
    }
};
// 递归解法
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL){
            return head;
        }
       ListNode* cur = reverseList(head->next);
       head->next->next = head;
       head->next = NULL;
       return cur;
    }
};