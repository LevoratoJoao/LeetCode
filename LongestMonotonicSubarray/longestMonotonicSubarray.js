/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    let inc = 1;
    let dec = 1;
    let max_length = 1;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            dec += 1;
            inc = 1;
        } else if (nums[i] < nums[i + 1]) {
            inc += 1;
            dec += 1;
        } else {
            inc = 1;
            dec = 1;
        }
        max_length = Math.max(max_length, inc, dec);
    }
    return max_length
};