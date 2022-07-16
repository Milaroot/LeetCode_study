class Solution:
    def __init__(self):
        self.mp = defaultdict(int)
    
    def DFS(self, m, n, row, col, move):
        if m >= row or n >= col or m < 0 or n < 0: return 1
        if move == 0: return 0
        curr = 0
        if self.mp[(m, n, move)] != 0: return self.mp[(m, n, move)] - 1
        
        #DFS h3r3
        curr += self.DFS(m + 1, n, row, col, move - 1)
        curr += self.DFS(m - 1, n, row, col, move - 1)
        curr += self.DFS(m, n + 1, row, col, move - 1)
        curr += self.DFS(m, n - 1, row, col, move - 1)
        curr %= (int(1e9) + 7)
        
        self.mp[(m, n, move)] = curr + 1
        return curr
        
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.DFS(startRow, startColumn, m, n, maxMove) 
        