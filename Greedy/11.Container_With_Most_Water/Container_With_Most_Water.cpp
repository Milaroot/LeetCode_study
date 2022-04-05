class Solution {
public:
    int maxArea(vector<int>& h) {
        int l = 0, r = h.size() - 1;
        int mx_water = 0;
        while(l < r){
            mx_water = max(min(h[l], h[r]) * (r - l), mx_water);
            if(h[l] < h[r]) l++;
            else r--;
        }
        return mx_water;
    }
};