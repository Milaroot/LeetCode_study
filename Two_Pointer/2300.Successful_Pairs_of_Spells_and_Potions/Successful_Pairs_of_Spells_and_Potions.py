class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], s: int) -> List[int]:
        ans = []
        potions.sort()
        potions_length = len(potions)
        for i in spells:
            target = s / i
            l = 0; r = len(potions) - 1
            idx = -1
            while(l <= r):
                mid = l + (r - l) // 2
                if potions[mid] >= target:
                    idx = mid
                    r = mid - 1
                else: l = mid + 1
            if idx == -1: ans.append(0)
            else: ans.append(potions_length - idx)
        return ans
                    