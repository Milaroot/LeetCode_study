class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0); flowerbed.append(0)
        ans = 0
        for i in range(1, len(flowerbed) - 1):
            if not(flowerbed[i - 1]) and not(flowerbed[i]) and not(flowerbed[i + 1]): 
                flowerbed[i] = 1
                ans += 1
        return ans >= n