# Leetcode_118_Pascal's_Triangle

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2:**

```
Input: numRows = 1
Output: [[1]]
```

**Constraints:**

- `1 <= numRows <= 30`

## Solution:

第一步 我們可以建立一新二維陣列。

第二步 每層頭都放入1，之後遍歷上層並將目前層數N位置放入上層N - 1 + N的值，

最後尾部放入1。

第三步 將建立好的一層放入二維陣列中，建立好測資需要的層數回傳。

## Code:

Python

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1],[1,2,1]];s = 0
        if numRows < 4 : return ans[:numRows]
        for i in range(numRows - 3):
            s = 0;curr = [1]
            for j in range(len(ans[-1])-1):
                curr.append(ans[-1][s] + ans[-1][s+1])
                s += 1
            curr.append(1)
            ans.append(curr)
        return ans
```

CPP

```cpp
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
```