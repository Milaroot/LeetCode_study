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
    ListNode* sortList(ListNode* head) {
        vector<int> arr;
        ListNode* ans = head;
        ListNode* root = head;
        while(root){
            arr.push_back(root->val);
            root = root->next;
        }
        
        sort(arr.begin(), arr.end());
        
        int curr = 0;
        
        while(ans){
            ans->val = arr[curr];
            curr++;
            ans = ans->next;
        }
        
        return head;
        
    }
};