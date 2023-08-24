package leetCode;

import java.util.Arrays;
import java.util.Stack;

public class Remoce_Duplicates_from_SortedArr {
    public static void main(String[] args) {
        removeDuplicates( new int[]{0,0,1,1,1,2,2,2,3,3,3,4});
    }

    private static int removeDuplicates(int [] arr) {
        Stack<Integer> stack = new Stack<>();
       for(int i=0; i<arr.length; i++){
           if (i >0 && stack.peek() == arr[i]) {
               stack.pop();
           }
           stack.add(arr[i]);
       }
        System.out.printf(Arrays.toString(stack.toArray()));
        System.out.printf(String.valueOf(stack.size()));
        return 1;
    }
}
