package leetCode;

import java.util.Arrays;
import java.util.stream.IntStream;

public class mergeSort {
    public static void main(String[] args) {
        merge(new int[]{1, 2, 3, 0, 0, 0},3, new int[]{2, 5, 6},3);
       // merge(new int[]{1},1, new int[]{},0);
        //merge(new int[]{0},0, new int[]{1},1);
    }
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        if(m>0 && m+n >= m) {
            for (int i = m; i < nums1.length; i++) {
                nums1[i] = nums2[i - m];
            }
            int [] copy = new int[nums1.length];
            mergeSort(nums1,copy,0,nums1.length-1);
            System.out.print(Arrays.toString(nums1));
        }else{
            for(int i=m; i< nums1.length; i++){
                nums1[i] = nums2[i];
            }
            System.out.print(Arrays.toString(nums1));
        }
    }
    public static void mergeSort(int[] arr , int[] copy,int left , int right){
        if(left < right){
            int mid = (left + right) / 2;
            mergeSort(arr,copy,left,mid);
            mergeSort(arr,copy,mid+1, right);
            sorting(arr,copy,left,right,mid);
        }
    }
    public static void sorting(int[] arr, int[] copy, int left, int right, int mid){
        int p1 = left;
        int p2 = mid + 1;
        int idx = p1;

        while(p1<=mid || p2<= right){
            if(p1 <= mid && p2 <= right){
                if(arr[p1] <= arr[p2]){
                    copy[idx++] = arr[p1++];
                }else{
                    copy[idx++] = arr[p2++];
                }
            }else if (p1<=mid && p2 > right){
                copy[idx++] = arr[p1++];
            }else{
                copy[idx++] = arr[p2++];
            }
        }
        for (int i = left; i <=right ; i++) {
            arr[i] = copy[i];
        }

    }
}

