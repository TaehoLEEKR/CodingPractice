package leetCode;

import java.util.Arrays;
import java.util.Stack;

public class Remoce_Duplicates_from_SortedArr2 {

    public static void main(String[] args) {
        removeDuplicates( new int[]{0,0,1,1,1,1,2,3,3});
    }

    private static int removeDuplicates(int [] arr) {
        Stack<Integer> stack = new Stack<>();
        int idx = 0;
        for(int i=0; i<arr.length; i++){
            if (i >0 && stack.peek() == arr[i] && idx >= 2) {
                stack.pop();
                idx = 0;
            }
            stack.add(arr[i]);
            idx++;
        }
        System.out.printf(Arrays.toString(stack.toArray()));
        System.out.printf(String.valueOf(stack.size()));
        return 1;
    }
}
