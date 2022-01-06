class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        int mp[1000] = {0}, left, right;
        for(int i = 0; i < size(trips); i++){
            left = trips[i][1], right = trips[i][2];
            int nm = trips[i][0];
            for(int l = left; l < right; l++){
                mp[l] += nm;
                if(mp[l] > capacity) return false;
            }
        }
        return true;
    }
};