package leetCode;

public class BestStock {
    public static void main(String[] args) {
        maxProfit(new int[] {7,1,5,3,6,4});
    }
    public static int maxProfit(int[] price){
        int minPrice = Integer.MAX_VALUE;
        int maxProift = Integer.MIN_VALUE;

        for(int pr : price){
            if(pr < minPrice ){
                minPrice = pr;
            } else if (pr - minPrice > maxProift) {
                maxProift = pr - minPrice;
            }
        }
        return maxProift;
    }
}
