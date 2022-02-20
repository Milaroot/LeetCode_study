class Solution {
public:
    void DFS(vector<vector<char>>& grid, int i, int j){
        grid[i][j] = '$';
        
        
        if(i > 0 && grid[i - 1][j] == '1') DFS(grid, i - 1, j);

        if(i < grid.size() - 1 && grid[i + 1][j] == '1') DFS(grid, i + 1, j);

        if(j > 0 && grid[i][j - 1] == '1') DFS(grid, i, j - 1);

        if(j < grid[i].size() - 1 && grid[i][j + 1] == '1') DFS(grid, i, j + 1);

    }
    
    
    
    
    int numIslands(vector<vector<char>>& grid) {
        
        int ans = 0;
        
        for(int x = 0; x < grid.size(); x++){
            
            for(int y = 0; y < grid[x].size(); y++){
                
                if(grid[x][y] == '1'){
                    ans++;
                    DFS(grid, x, y);
                }
            
            }
        }
        return ans;
    }
};