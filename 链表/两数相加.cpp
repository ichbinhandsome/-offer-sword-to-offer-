/*
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(-1);
        ListNode* curr = head;
        int count = 0;
        while (l1!=NULL || l2!=NULL || count!=0){
            int v = 0;
            if (l1!=NULL){
                v += l1->val;
                l1 = l1->next;
            }
            if (l2!=NULL){
                v += l2->val;
                l2 = l2->next;
            }
            v += count;
            count = v>=10?1:0;
            curr->next = new ListNode(v%10);
            curr = curr->next;
        }
        return head->next;
    }
};