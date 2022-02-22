class Solution {
public:
    int titleToNumber(string columnTitle) {
        int total = 0; 
        for(char & c: columnTitle){
            total *= 26;
            total += c - 64;
        }
        return total;
    }
};