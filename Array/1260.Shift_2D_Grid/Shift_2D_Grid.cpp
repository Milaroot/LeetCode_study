class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        vector<int> total;
        int tol = 0;
        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < grid[i].size(); ++j){
                total.push_back(grid[i][j]);
                tol++;
            }
        }
        k %= tol;
        if(k == 0) return grid;
        while(k){
            int last = total[tol - 1];
            total.pop_back();
            total.insert(total.begin(), last);
            k--;
        }
        int curr = 0;
        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < grid[i].size(); ++j){
                grid[i][j] = total[curr];
                curr++;
            }
        }
        return grid;
    }
};