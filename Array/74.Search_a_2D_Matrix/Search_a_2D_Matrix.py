class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check(m, t):
            if m[0] > t: return True
        
        
        
        def y_bs(m, t):
            ans = len(m)
            l = 0; r = len(m) - 1
            while(l <= r):
                mid = l + (r - l) // 2
                if check(m[mid], t):
                    ans = mid
                    r = mid - 1
                else: l = mid + 1
            return ans - 1
        
        
        
        def x_bs(m, t):
            l = 0; r = len(m) - 1
            while(l <= r):
                mid = l + (r - l) // 2
                if m[mid] == t: return True
                elif m[mid] > t: r = mid - 1
                else: l = mid + 1
            return False
        
        if len(matrix) > 1: 
            ta = y_bs(matrix, target)
            if ta < 0 : return False
            res = x_bs(matrix[ta], target)
        else: res = x_bs(matrix[0], target)

        
        return res
        
            
            