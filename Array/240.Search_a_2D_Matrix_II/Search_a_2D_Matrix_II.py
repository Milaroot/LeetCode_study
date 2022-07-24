class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target: break
            if row[-1] < target: continue
            l = 0; r = len(row) - 1
            while(l <= r):
                mid = l + (r - l) // 2
                if row[mid] < target: l = mid + 1
                elif row[mid] > target: r = mid - 1
                else: return True
        return False