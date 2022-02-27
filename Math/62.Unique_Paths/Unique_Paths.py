class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0] = 1
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i > 0: dp[i][j] += dp[i - 1][j]
                if j > 0: dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]