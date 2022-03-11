# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not(head): return head
        
        
        prev = None
        
        arr = deque()
        
        
        ans = root = head
        
        while(head): 
            arr.append(head.val)
            head = head.next
        
        k %= len(arr)
        
        for i in range(k):
            arr.appendleft(arr.pop())
        
        while(root):
            root.val = arr.popleft()
            root = root.next
        return ans
        