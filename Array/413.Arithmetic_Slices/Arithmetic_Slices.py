class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: return 0
        
        diff = nums[1] - nums[0]; cnt = 2; ans = 0
        
        for i in range(2, len(nums)):
            
            if(nums[i] - nums[i - 1] == diff):
                cnt += 1
                
            else:
                
                if(cnt >= 3):
                    cnt -= 2
                    ans += (pow(cnt , 2) + cnt) // 2
                     
                diff = nums[i] - nums[i - 1]
                cnt = 2
                
        
        if cnt >= 3:
            cnt -= 2
            ans += (pow(cnt , 2) + cnt) // 2
            
        return ans
    