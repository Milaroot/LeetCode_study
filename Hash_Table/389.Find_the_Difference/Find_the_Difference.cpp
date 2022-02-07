class Solution {
public:
    char findTheDifference(string s, string t) {
        int curr = 0;
        for(char i: s) curr ^= i;
        for(char j: t) curr ^= j;
        return curr;
    }
};