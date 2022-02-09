class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = []
        hash_map = defaultdict(int)
        for i in nums:
            if hash_map[i - k] != 0:
                ans.append(sorted([i, i - k]))
            if hash_map[i + k] != 0:
                ans.append(sorted([i, i + k]))
            hash_map[i] += 1
        ans = set([tuple(i) for i in ans])

        return len(ans)