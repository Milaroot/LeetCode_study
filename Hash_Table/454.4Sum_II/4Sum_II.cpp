class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int ans = 0;
        unordered_map<int,int> hash_map;
        for(int i: nums1){
            for(int j: nums2){
                hash_map[i + j]++;
            }
        }
        for(int k: nums3){
            for(int l: nums4){
                int flag = hash_map[-1 * (k + l)];
                if(flag) ans += flag;
            }
        }
        return ans;
    }
};