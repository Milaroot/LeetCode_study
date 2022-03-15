class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> stk;
        string ans;
        for(int i = 0; i < s.size();i++){
            if(s[i] == '(') stk.push_back(i);
            else if(s[i] == ')'){
                if(stk.size() == 0){
                    s[i] = '$';
                }
                else{
                    stk.pop_back();
                }
            }
        }
        
        for(int i = 0; i < stk.size(); i++){
            s[stk[i]] = '$';
        }
        
        for(char i: s){
            if(i != '$') ans += i;
        }
        
        return ans;
        
    }
};