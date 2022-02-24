# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        ans = head
        arr = []
        while(root):
            arr.append(root.val)
            root = root.next
        
        arr.sort()
        curr = 0
        
        while(ans):
            ans.val = arr[curr]
            ans = ans.next
            curr += 1
        
        
        return head
        