class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        vector<int> monotonic_stk = {};
        long long int ans = 0, curr = 48763;
        for(int i = 0; i <= arr.size(); i++){
            if(i == arr.size()) curr = -1;
            else curr = arr[i];
            while(monotonic_stk.size() > 0 && arr[monotonic_stk[monotonic_stk.size() - 1]] > curr){
                long long int m = monotonic_stk[monotonic_stk.size() - 1], l;
                monotonic_stk.pop_back();
                if(monotonic_stk.size() == 0) l = -1;
                else l = monotonic_stk[monotonic_stk.size() - 1];
                ans = (ans + (arr[m] * (m - l) * (i - m))) % 1000000007;
            }
            monotonic_stk.push_back(i); 
        }
        return ans;
    }
};