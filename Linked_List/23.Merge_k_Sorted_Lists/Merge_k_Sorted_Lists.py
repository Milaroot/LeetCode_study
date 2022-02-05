# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total = []
        for i in lists:
            head = i
            while(head != None):
                total.append(head.val)
                head = head.next
        total = sorted(total)[::-1]
        
        nx = None
        for i in total:
            Node = ListNode()
            Node.val = i
            Node.next = nx
            nx = Node
        return nx