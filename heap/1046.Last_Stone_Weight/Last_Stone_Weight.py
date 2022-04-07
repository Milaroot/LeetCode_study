class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda i: -i, stones))
        heapq.heapify(stones)
        while(len(stones) > 1):
            mx1, mx2 = -heapq.heappop(stones), -heapq.heappop(stones)
            tmp = abs(mx1 - mx2)
            if tmp != 0: heapq.heappush(stones, -tmp)
        if len(stones) == 0: return 0
        else: return -stones[0]