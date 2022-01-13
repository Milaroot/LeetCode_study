class Solution:
    def findMinArrowShots(self, arr: List[List[int]]) -> int:
        if len(arr) == 1: return 1
        arr.sort(key= lambda i: i[1])
        ans = []
        ans.append([arr[0][0], arr[0][1]])
        for j in range(1, len(arr)):
            curr = arr[j]
            prev = ans[-1]
            if curr[0] <= prev[1]:
                prev = [max(curr[0], prev[0]), min(curr[1],prev[1])]
            else:
                ans.append(curr)
        return len(ans)
                