/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* before = dummy;
        for(int i = 0; i<left-1; i++) before = before->next; 
        ListNode* l = before->next;
        ListNode* prev = nullptr;
        ListNode* curr = l;
        for(int i = left; i<right+1; i++){
            ListNode* nxt = curr->next; 
            curr->next = prev;
            prev = curr; 
            curr = nxt; 
        }

        before->next = prev;
        l->next = curr;
        return dummy->next;
    }
};