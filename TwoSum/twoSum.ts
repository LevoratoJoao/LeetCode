function twoSum(nums: number[], target: number): number[] {
    let hashMap: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (hashMap.has(nums[i])) {
            return [hashMap.get(target - nums[i])!, i];
        }
        hashMap.set(target - nums[i], i);
    }
    return [];
};

console.log(twoSum([2,7,11,15], 9));
