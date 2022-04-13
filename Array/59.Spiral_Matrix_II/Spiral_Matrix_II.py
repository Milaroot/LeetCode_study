class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0 for j in range(n)] for i in range(n)]
        x = n - 1; y = n
        curr = 0
        curr_x = 0;curr_y = -1
        while(1):
            # ⇨
            if  x > 0 or y > 0:
                for i in range(y):
                    curr_y += 1                   
                    curr += 1
                    arr[curr_x][curr_y] = curr
                y -= 1
            else: break
            # ⇩
            if  x > 0 or y > 0:
                for i in range(x):
                    curr_x += 1
                    curr += 1
                    arr[curr_x][curr_y] = curr
                x -= 1
            else: break
            # ⇦   
            if  x > 0 or y > 0:
                for i in range(y):
                    curr_y -= 1
                    curr += 1
                    arr[curr_x][curr_y] = curr
                y -= 1
            else: break
            # ⇧ 
            if  x > 0 or y > 0:
                for i in range(x):
                    curr_x -= 1
                    curr += 1
                    arr[curr_x][curr_y] = curr
                x -= 1
            else: break
                
        return arr