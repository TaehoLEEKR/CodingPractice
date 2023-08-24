package leetCode;

public class BestStock2 {
    public static void main(String[] args) {
        bestStock(new int[]{7,1,2,3,4,5});
    }

    private static int bestStock(int[] prices) {
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                maxProfit += prices[i] - prices[i - 1];
            }
        }
        return maxProfit;
    }
}
