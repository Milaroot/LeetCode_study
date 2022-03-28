class Solution {
    public char findTheDifference(String s, String t) {
        int curr = 0;
        for(int i = 0; i < s.length(); ++i) curr ^= s.charAt(i);
        for(int i = 0; i < t.length(); ++i) curr ^= t.charAt(i);
        return (char)curr;
    }
}