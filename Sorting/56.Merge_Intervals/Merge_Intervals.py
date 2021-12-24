class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        ans = []
        arr.sort()
        arr_start = arr[0][0]; arr_end = arr[0][1]
        for i in range(1, len(arr)):
            if arr[i][0] <= arr_end: 
                if arr[i][1] > arr_end:
                    arr_end = arr[i][1]
            else:
                ans.append([arr_start, arr_end])
                arr_start = arr[i][0]
                arr_end = arr[i][1]
        ans.append([arr_start, arr_end])
        return ans