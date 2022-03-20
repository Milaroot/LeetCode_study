class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        last = -1111
        for i in nums:
            if i != last: 
                arr.append(i)
                last = i
                
        ans = 0
        for i in range(1, len(arr) - 1):
            
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]: ans += 1
            if arr[i - 1] > arr[i] and arr[i] < arr[i + 1]: ans += 1

        return ans