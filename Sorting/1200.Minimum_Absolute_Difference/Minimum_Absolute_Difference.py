class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_dif = float("inf")
        ans = []
        arr = sorted(arr)
        for i in range(1, len(arr)):
            curr_dif = arr[i] - arr[i - 1]
            if  curr_dif < min_dif: 
                ans = [[arr[i - 1], arr[i]]]
                min_dif = curr_dif
            elif curr_dif == min_dif:
                ans.append([arr[i - 1], arr[i]])
        return ans