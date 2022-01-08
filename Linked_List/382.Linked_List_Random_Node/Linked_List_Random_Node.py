# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        self.lng = 0
        while(head):
            self.lng += 1
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.arr[randint(0, self.lng - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()