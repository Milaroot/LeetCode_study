# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_map = defaultdict(int)
        
        while(head):
            if hash_map[id(head)] != 0: return True
            hash_map[id(head)] += 1
            head = head.next
        return False