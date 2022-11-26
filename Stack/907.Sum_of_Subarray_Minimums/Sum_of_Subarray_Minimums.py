class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        monotonic_stk = []; ans = 0
        for i in range(len(arr) + 1):
            if(i == len(arr)): curr = -1
            else: curr = arr[i]
            while(len(monotonic_stk) > 0 and arr[monotonic_stk[-1]] > curr):
                m = monotonic_stk.pop(); l = 0
                if(len(monotonic_stk) == 0): l = -1
                else: l = monotonic_stk[-1]
                ans += (arr[m] * (m - l) * (i - m))
            monotonic_stk.append(i);      
        return ans % (int(1e9) + 7);
    
