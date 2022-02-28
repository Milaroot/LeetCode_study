class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0: return []
        ans = []
        tmp = [nums[0]]
        for i in range(1, len(nums)):
            if tmp != [] and nums[i] != tmp[-1] + 1:
                if len(tmp) > 1:
                    ans.append(f"{tmp[0]}->{tmp[-1]}")
                    tmp = []
                else: 
                    ans.append(str(tmp[0]))
                    tmp = []
                
            tmp.append(nums[i])
        
        if len(tmp) > 1:
            ans.append(f"{tmp[0]}->{tmp[-1]}")
            tmp = []
        elif tmp != []: 
            ans.append(str(tmp[0]))
            tmp = []
            
        return ans
                
            
            