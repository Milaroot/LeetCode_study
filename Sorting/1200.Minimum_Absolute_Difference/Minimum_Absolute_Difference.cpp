class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        int min_diff = numeric_limits<int>::max();
        vector<vector<int>> ans;
        sort(arr.begin(), arr.end());
        for(int i = 1; i < arr.size(); i++){
            int curr_diff = arr[i] - arr[i - 1];
            if(curr_diff < min_diff){
                min_diff = curr_diff;
                ans = {{arr[i - 1], arr[i]}};
            }
            else if (curr_diff == min_diff){
                ans.push_back({arr[i - 1], arr[i]});
            }
        }
        return ans;
    }
};
