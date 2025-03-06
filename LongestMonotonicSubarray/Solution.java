class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int max_length = 1;
        int inc = 1;
        int dec = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                dec += 1;
                inc = 1;
            } else if (nums[i] < nums[i + 1]) {
                inc += 1;
                dec = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            max_length = Math.max(max_length, Math.max(inc, dec));
        }

        return max_length;
    }
}