import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * [2,7,11,15]
     *
     * { 7: 0 }
     * { : 1 }
     * { 2: 2 }
     * { 7: 3 }
     *
     */
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                Integer first = map.get(nums[i]);
                Integer seccond = i;
                return new int[] { first, seccond };
            }
            map.put(target - nums[i], i);
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        int[] arr = twoSum(new int[]{2,7,11,15}, 9);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
