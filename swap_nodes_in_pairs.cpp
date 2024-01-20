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
    ListNode* swapPairs(ListNode* head) {
        bool is_even = true;
        ListNode* it = head;
        ListNode* prev_it;
        ListNode* ret_pointer;
        
        if (it == nullptr) { 
            ret_pointer = it;
        } else if(it->next != nullptr) {
            ret_pointer = it->next;
        } else {
            ret_pointer = it;
        }

        while (it != nullptr && (it->next) != nullptr) {
            ListNode* temp = (it->next)->next;

            if (it != head) {
                prev_it->next = it->next;
            }

            (it->next)->next = it;
            it->next = temp;
            prev_it = it;
            it = it->next;
        }

        return ret_pointer;
    }
};
