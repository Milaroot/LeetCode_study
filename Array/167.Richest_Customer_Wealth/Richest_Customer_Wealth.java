class Solution {
    public int maximumWealth(int[][] accounts) {
        int richest = -1;
        for (int i = 0; i < accounts.length; i++) {
            int curr = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                curr += accounts[i][j];
            }
            richest = Math.max(richest, curr);
        }
        return richest;
    }
}