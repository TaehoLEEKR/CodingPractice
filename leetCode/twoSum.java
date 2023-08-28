package leetCode;

import java.util.Arrays;

public class twoSum {
    public static int[] twoSum1(int[] numbers, int target) {

        int left = 0;
        int right = numbers.length - 1;

        while (left < right){
            if(numbers[left] + numbers[right] > target ){
                right --;
            }else if (numbers[left] + numbers[right] < target){
                left++;
            }else{
                return new int[] {left+1 ,right+1};
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString( twoSum1(new int[] {2,7,11,15},18 )));
        System.out.println(Arrays.toString( twoSum1(new int[] {-1,0},-1 )));
        System.out.println(Arrays.toString( twoSum1(new int[] {2,3,4},6 )));
    }
}
