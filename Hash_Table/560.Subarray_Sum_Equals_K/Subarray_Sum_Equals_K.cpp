class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        int ans = 0, curr = 0;
        mp[0]++;
        for(int i: nums){
            curr += i;
            ans += mp[curr - k];
            mp[curr]++;
        }
        return ans;
    }
};