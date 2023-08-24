package leetCode;

import java.util.ArrayDeque;
import java.util.Deque;

public class RotateArray {
    public static void main(String[] args) {
        rotateArray(new int[]{1,2,3,4,5,6,7} , 3);
    }

    private static void rotateArray(int[] arr, int k) {
        Deque<Integer> deq = new ArrayDeque<>();

        for(int i: arr){
            deq.add(i);
        }
        for(int i=0; i<k; i++){
            int popItem = deq.removeLast();
            deq.addFirst(popItem);
        }
        for(int i = 0; i<arr.length; i++){
            arr[i] = deq.poll();
        }

    }

}
