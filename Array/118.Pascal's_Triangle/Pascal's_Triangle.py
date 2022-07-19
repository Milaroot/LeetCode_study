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