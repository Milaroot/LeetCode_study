class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0); flowerbed.push_back(0);
        int ans = 0;
        for(int i = 1; i < size(flowerbed) - 1; i++){
            if (!flowerbed[i - 1] && !flowerbed[i] && !flowerbed[i + 1]){ 
                flowerbed[i] = 1;
                ans += 1;
            }
        }
        return ans >= n;
    }
};