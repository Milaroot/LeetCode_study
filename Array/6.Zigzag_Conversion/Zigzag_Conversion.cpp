class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        vector<string> arr(numRows);
        int curr = 0, flag = 0;
        
        for(auto &i : s){
            if(curr == 0) flag = 0;
            arr[curr] += i;
            
            if(flag == 0) curr++;
            else curr--;
            if(curr == numRows) {
                flag = 1;
                curr -= 2;
            }
        }
        string ans;
        for(int i = 0; i < size(arr); ++i){
            for(int j = 0; j < size(arr[i]); ++j){
                ans += arr[i][j];
            }
        }
        return ans;
        
    }
};