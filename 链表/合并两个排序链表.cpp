/*
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1==NULL) return l2;
        if (l2==NULL) return l1;
        //递归
        // if (l1->val < l2->val){
        //     l1->next = mergeTwoLists(l1->next, l2);
        //     return l1;
        // }
        // else{
        //     l2->next = mergeTwoLists(l1, l2->next);
        //     return l2;
        // }
        //迭代
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        while (l1 && l2){
            if (l1->val < l2->val){
                curr->next = l1;
                curr = curr->next;
                l1 = l1->next;
            }
            else{
                curr->next = l2;
                curr = curr->next;
                l2 = l2->next;
            }
        }
        if (l1 == NULL){
            curr->next = l2;
        }else{
            curr->next = l1;
        }
        return dummy->next;

    }
};