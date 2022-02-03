class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        hash_map = defaultdict(int)
        for i in nums1:
            for j in nums2:
                hash_map[i + j] += 1
        
        for k in nums3:
            for l in nums4:
                flag = hash_map[-1 * (k + l)]
                if flag: ans += flag
        return ans