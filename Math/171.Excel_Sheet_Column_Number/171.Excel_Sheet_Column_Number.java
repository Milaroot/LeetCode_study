class Solution {
    public int titleToNumber(String columnTitle) {
        int total = 0;
        for (int i = 0; i < columnTitle.length(); i++) {
            total *= 26;
            total += (int) columnTitle.charAt(i) - 64;
        }
        return total;
    }
}