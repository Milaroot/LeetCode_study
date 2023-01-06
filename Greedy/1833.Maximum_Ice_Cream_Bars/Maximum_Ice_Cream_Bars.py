class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if costs[0] > coins: return 0
        for i in range(1, len(costs)):
            costs[i] += costs[i - 1]
            if costs[i] > coins: return i
        return len(costs)
                