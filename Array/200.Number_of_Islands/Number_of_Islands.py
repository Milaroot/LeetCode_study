class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        
        def dfs(i, j):
            grid[i][j] = "$" 
    
            if i > 0 and grid[i - 1][j] == "1": dfs(i - 1, j)
            if i < len(grid) - 1  and grid[i + 1][j] == "1":  dfs(i + 1, j)
            if j > 0  and grid[i][j - 1] == "1": dfs(i, j - 1)
            if j < len(grid[i]) - 1 and grid[i][j + 1] == "1": dfs(i, j + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
                    
        
        return ans