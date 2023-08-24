package leetCode;

public class JumpGame {
    public static void main(String[] args) {
        jump(new int[]{2,3,1,1,4});
    }

    private static boolean jump(int[] nums) {
        int curr = 0;
        int lastIdx = nums.length - 1;
        int maxJmp = 0;
        for (int i = 0; i <lastIdx; i++) {
            if(curr < i ){
                return  false;
            }
            maxJmp = i + nums[i];
            if(maxJmp > curr){
                curr = maxJmp;
            }
            if(curr >= lastIdx){
                return true;
            }
        }
        return true;
    }
}
