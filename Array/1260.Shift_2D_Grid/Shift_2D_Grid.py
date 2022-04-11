class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        total = []
        tol = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                total.append(grid[i][j])
                tol += 1
        k %= tol
        for i in range(k): total.insert(0, total.pop())
        curr = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = total[curr]
                curr += 1
        return grid