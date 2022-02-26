
class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1: return nums[0]
        
        if ln == 2: return max(nums)
        
        
        
        
        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)
        
        dp1[0] = nums[1]
        dp1[1] = max(nums[1], nums[2])
        dp2[0] = nums[-2]
        dp2[1] = max(nums[-2], nums[-3])
        

        
        if ln == 3: return max(dp1[-1],dp2[-1])
        
        #left to right
        
        for i in range(3, len(nums)):
            dp1[i - 1] = max(dp1[i - 3] + nums[i], dp1[i - 2])
        
        #right to left
        for j in range(4, len(nums) + 1):
            dp2[j - 2] = max(dp2[j - 4] + nums[-j], dp2[j - 3])
        
        return max(dp1[-1], dp2[-1])
            