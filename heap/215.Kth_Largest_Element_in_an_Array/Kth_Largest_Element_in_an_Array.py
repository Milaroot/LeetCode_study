class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for i in nums:
            heapq.heappush(hp, -i)
        for i in range(k - 1):
            heapq.heappop(hp)
        return heapq.heappop(hp) * -1