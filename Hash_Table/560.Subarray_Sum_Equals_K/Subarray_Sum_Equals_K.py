class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        curr = 0
        ans = 0
        hash_map[0] = 1
        for i in nums:
            curr += i
            ans += hash_map[curr - k]
            hash_map[curr] += 1
        return ans