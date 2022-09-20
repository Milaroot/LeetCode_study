# LeetCode_718_Maximum_Length_of_Repeated_Subarray

Given two integer arrays `nums1`and `nums2`
, return *the maximum length of a subarray that appears in **both** arrays*.

**Example 1:**

```
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

```

**Example 2:**

```
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 100`

這題的測資給到nums.length ≤ 1000，所以我們盡量將複雜度控制在O(n^ 2)以下

根據觀察和簡化我們要找到同時出現在兩個陣列中最大長度的subarray

我們可以使用2維DP來記錄過程

```python
dp = [[0 for i in range(len(nums2) + 1)]
```

利用兩個for迴圈來進行比較

```python
for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
```

並將nums1[I][J]和nums2[I][J]的數字從後往前比較並加上DP[I +1 ][j + 1]，並且存到DP表中



dp表中最大的的元素就是答案了


<h1>Code</h1>

```python

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp, ans = [[0 for i in range(len(nums2) + 1)] for i in range(len(nums1) + 1)], 0
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]: dp[i][j] = 1 + dp[i + 1][j + 1]
                ans = max(ans, dp[i][j])
        return ans
```