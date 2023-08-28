package leetCode;

import java.util.HashSet;
import java.util.Set;

public class leetCode_3 {
    public static int lengthOfLongestSubstring(String s) {
        int maxLength = Integer.MIN_VALUE;
        int left = 0;
        int right = 0;
        Set<Character> sets = new HashSet<>();

        while (right < s.length()) {
            if (!sets.contains(s.charAt(right))) {
                sets.add(s.charAt(right));
                maxLength = Math.max(maxLength, sets.size());
                right++;
            } else {
                sets.remove(s.charAt(left));
                left++;
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        lengthOfLongestSubstring("abcabcbb");
    }
}
