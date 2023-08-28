package leetCode;

import java.util.Arrays;

public class MinimumsummarySum {
    public static int minSubArrayLen(int target, int[] nums) {
            int minLen = 0;
            int p1 = 0;
            int sum = 0;

            for (int i = 0; i < nums.length; i++) {
                sum += nums[i];

                while (sum >= target) {
                    minLen = Math.min(minLen, i - p1 + 1);
                    sum -= nums[p1];
                    p1++;
                }
            }
            if(minLen == 0){
                return 0;
            }else {
                return minLen;
            }
    }

    public static void main(String[] args) {
        minSubArrayLen(7,new int[] {2,3,1,2,4,3});
    }
}
