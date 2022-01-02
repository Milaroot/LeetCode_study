class Solution:
    def numPairsDivisibleBy60(time: list) -> int:
        hash_map = [0] * 60
        ans = 0
        for i in time: hash_map[i % 60] += 1
        for num in time:
            hash_map[num % 60] -= 1
            ans += hash_map[0 if num % 60 == 0 else 60 - num % 60]
        return ans

