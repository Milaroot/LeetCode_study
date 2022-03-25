class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = sorted(costs, key = lambda i: i[0] - i[1])
        ans = 0
        for i in range(len(arr) // 2): ans += arr[i][0]
        for i in range(len(arr) // 2, len(arr)): ans += arr[i][1]
        return ans
            
            