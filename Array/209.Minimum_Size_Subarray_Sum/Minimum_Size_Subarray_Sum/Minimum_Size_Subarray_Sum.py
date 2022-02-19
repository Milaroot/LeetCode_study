class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn = int(1e6) + 1
        curr = 0
        total = 1
        l = 0; r = 1
        curr += nums[0]
        
        if curr >= target: return 1
        
        for i in range(r, len(nums)):
            curr += nums[i]
            total += 1
            while(curr >= target):
                mn = min(mn, total)
                if total == 1: return 1
                curr -= nums[l]
                total -= 1
                l += 1
        
        if mn == int(1e6) + 1: return 0
        return mn
                
                
                
        