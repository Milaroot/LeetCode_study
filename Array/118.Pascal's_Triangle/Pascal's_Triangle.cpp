class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if(numRows == 1) return {{1}};
        vector<vector<int>> dp = {{1}, {1, 1}};
        vector<int> tmp;
        for(int i = 2; i < numRows; ++i){
            tmp.clear();
            tmp.push_back(1);
            for(int j = 1; j < dp[i - 1].size(); ++j)
                tmp.push_back(dp[i - 1][j] + dp[i - 1][j - 1]);
            tmp.push_back(1);
            dp.push_back(tmp);
        }
        return dp;
    }
};