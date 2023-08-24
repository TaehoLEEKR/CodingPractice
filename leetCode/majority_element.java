package leetCode;

import java.util.HashMap;
import java.util.Map;

public class majority_element {
    public static void main(String[] args) {
        majorityElement(new int[]{2,2,1,1,1,2,2});
    }
    public static int majorityElement(int[] nums) {
        int majorityNum = nums.length / 2;
        Map<Integer,Integer> countMap = new HashMap<>();
        for(int i : nums){
            countMap.put(i,countMap.getOrDefault(i,0)+1);
            if(countMap.get(i) > majorityNum){
                return i;
            }
        }
        return 0;
    }
}
