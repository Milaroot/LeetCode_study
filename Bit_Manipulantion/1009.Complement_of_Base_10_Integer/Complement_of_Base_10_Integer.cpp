class Solution {
public:
    int bitwiseComplement(int n) {
        vector<int> b;
        int ans = 0;
        while(n >= 2){
            n % 2 == 1 ? b.push_back(0) : b.push_back(1);
            n /= 2;
        }
         n == 1 ? b.push_back(0) : b.push_back(1);
        reverse(b.begin(), b.end());
        for(auto i: b){
            ans *= 2;
            ans += i;
        }
        return ans;
    }
};