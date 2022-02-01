class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0, mn = 1000000;
        for (int price : prices) {
            if (mn < 1000000 && price > mn)
                ans = Math.max(ans, price - mn);
            if (price < mn)
                mn = price;
        }
        return ans;
    }
}