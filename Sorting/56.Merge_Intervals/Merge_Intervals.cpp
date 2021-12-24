class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& arr) {
        vector<vector<int>> ans;
        sort(arr.begin(), arr.end());
        int arr_start = arr[0][0], arr_end = arr[0][1];
        for(int i = 1; i < size(arr); i++){
            if(arr[i][0] <= arr_end){
                if (arr[i][1] > arr_end){
                    arr_end = arr[i][1];
                }
            }
            else{
                ans.push_back({arr_start, arr_end});
                arr_start = arr[i][0];
                arr_end = arr[i][1];
            }
        }
        ans.push_back({arr_start, arr_end});
        return ans;
    }
};