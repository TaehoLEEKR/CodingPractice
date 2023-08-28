package leetCode;

import java.util.Arrays;

public class palindrome {

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
    }
    public static boolean isPalindrome(String s){
        String[] strs = s.toLowerCase().replaceAll("[^ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9]", "").split("");
        int left = 0;
        int right = strs.length-1;
        while (left < right){
            if(!strs[left].equals(strs[right])){
                return false;
            }
                left++;
                right--;
        }
        return true;
    }
}
