package leetCode;

import java.util.Arrays;

public class RemoveElement {
    public static int removeElement(int[] nums, int val) {
        return (int) Arrays.stream(nums)
                .filter(num -> num != val)
                .count();
    }

    public static void main(String[] args) {
        removeElement(new int[]{3,2,2,3},3);
    }
}
