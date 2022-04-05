class Solution {
    public int maxArea(int[] h) {
        int mx_water = 0;
        int l = 0, r = h.length - 1;
        while(l < r){
            int curr_water = (r - l) * Math.min(h[l], h[r]);
            mx_water = Math.max(curr_water, mx_water);
            if(h[l] < h[r]) l++;
            else r--;
        }
        return mx_water;
    }
}