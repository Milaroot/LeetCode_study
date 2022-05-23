class Solution {
public:
    int tribonacci(int n) {
        vector<int> dp = {0, 1, 1};
        int curr = 2;
        for(int i = 0; i < n - 2; i++){
            curr++;
            dp.push_back(dp[curr - 1] + dp[curr - 2] + dp[curr - 3]);
        }
        return dp[n];
    }
};