# LeetCode_576_Out_of_ Boundary_Paths

There is an `m x n` grid with a ball. The ball is initially at the position `[startRow, startColumn]`. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply **at most** `maxMove` moves to the ball.

Given the five integers `m`, `n`, `maxMove`, `startRow`, `startColumn`, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it **modulo** `109 + 7`.

**Constraints:**

- `1 <= m, n <= 50`
- `0 <= maxMove <= 50`
- `0 <= startRow < m`
- `0 <= startColumn < n`

## **Example 1:**

![https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png](https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png)

```
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
```

## **Example 2:**

![https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png](https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png)

```
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
```

## Solution:

我們可以看出題目的目標是使用DFS來尋找出可以越界的所有可能。

因此我們設計一個DFS函式

```python
def  def DFS(self, m, n, row, col, move):
```

接下來我們需要考慮如果使用單純的DFS進行尋找，在過程中可能會一直遇到已處理的位置，

造成TLE。

因此我們需要建立一個資料結構來記錄走過該點位置後的到的結果，在此後走到該位置時可以直接取得之前獲得的結果(記得要mod 10^9 + 7)

```python
def __init__(self):
	self.mp = defaultdict(int)
```

本解法以defaultdict結構

也可使用三維陣列來儲存

```python
def __init__(self):
	self.arr = [[[]]]
```

接下來就將起始位置放入DFS函式並進行動作之後回傳就可以得到答案了

## Code:

Python

```python
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
```