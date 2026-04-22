/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    let arr = [];
    for (let i of nums) {
        arr.push(nums[i]);
    }
    return arr;
};