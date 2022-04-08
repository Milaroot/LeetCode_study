class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.hp = nums
        self.target = k

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        for i in range(len(self.hp) - self.target): heapq.heappop(self.hp)
        print(self.hp)
        return self.hp[0]