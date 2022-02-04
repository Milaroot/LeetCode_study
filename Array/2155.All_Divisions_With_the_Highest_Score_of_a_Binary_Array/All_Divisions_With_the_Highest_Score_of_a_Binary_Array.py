class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        for i in nums: 
            if i == 1: right += 1
        mx = right
        mx_idx = [0]
        for i, num in enumerate(nums):
            
            if num == 1:
                right -= 1
            else:
                left += 1

            if mx == right + left: mx_idx.append(i + 1)
            elif mx < right + left: 
                mx = right + left
                mx_idx = [i + 1]
            
        return mx_idx